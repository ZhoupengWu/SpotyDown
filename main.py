import csv
import os
from re import sub
from pathlib import Path
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
scope = "user-library-read"

SONGS_TRACKER = "songs.csv"
DOWNLOAD_PATH = Path.home() / "my_spotify_song" # You can change the path of the directory where you download the songs

DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

if not os.path.exists(SONGS_TRACKER):
    with open(SONGS_TRACKER, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['song', 'artist'])

def getLikedSongs():
    results = sp.current_user_saved_tracks(limit=50)
    all_tracks = []

    while results:
        for item in results['items']:
            track = item['track']
            song_name = track['name']
            artist_name = track['artists'][0]['name']
            all_tracks.append(f"{song_name} by {artist_name}")

        if results['next']:
            results = sp.next(results)
        else:
            break

    return all_tracks

def getNewSong(song, artist):
    with open(SONGS_TRACKER, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([song, artist])

def getDownloadedSongs():
    if not os.path.exists(SONGS_TRACKER):
        return []
    
    downloaded_songs = []

    with open(SONGS_TRACKER, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        
        for row in reader:
            if len(row) < 2:
                continue

            song_name = row[0].strip()
            artist_name = row[1].strip()
            downloaded_songs.append(f"{song_name} by {artist_name}")

    return downloaded_songs

def downloadSong(song, artist):
    song_query = f"{song} by {artist}"
    search = VideosSearch(song_query, limit=1)
    
    try:
        result = search.result()['result'][0]
        youtube_url = result['link']
    except Exception as e:
        print(f"Youtube Search Issue: {e}")
        return

    safe_filename = sub(r'[\\/*?:"<>|]', '', song_query)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(DOWNLOAD_PATH / f"{safe_filename}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        print(f"Failed download song: {e}")

def main():
    liked_songs = getLikedSongs()
    downloaded_songs = getDownloadedSongs()
    new_songs = [song for song in liked_songs if song not in downloaded_songs]

    print(f"\nFound {len(new_songs)} new songs\n")
    
    for song in tqdm(new_songs, desc="Download", unit="song"):
        try:
            song_name, artist_name = song.split(' by ', 1)
            tqdm.write(f"Download: {song_name} of {artist_name}")
            downloadSong(song_name, artist_name)
            getNewSong(song_name, artist_name)
        except Exception as e:
            tqdm.write(f"Issue for '{song}': {e}")

if __name__ == '__main__':
    main()