# 🎵 SpotyDown

## 📑 Description

This python script allows to download automatically songs in your Liked Songs playlist, finding the best version on YouTube and saving as MP3 file on your folder

## ✨ Features

- Retrieves all your liked songs from your Spotify account
- Searches each song on YouTube
- Downloads the audio as MP3 using `yt-dlp` and `ffmpeg`
- Tracks already downloaded songs in a CSV file
- Supports resume: only downloads new songs added to your playlist

## ⚙️ Requirements

- **Python 3.8+**
- **Spotify account**
- **Installing FFmpeg**

  - **On Windows go to [release build](https://www.gyan.dev/ffmpeg/builds/)**

  - **On Linux (depends from the distributions)**
    ```bash
    sudo apt install ffmpeg
    ```
  - **On macOS**
    ```bash
    brew install ffmpeg
    ```
  - **On Termux**
    ```bash
    pkg install ffmpeg
    ```

## 🛠️ Installation and Setup

1. **Download or clone the repository**

    ```bash
    git clone
    ```

2. **Create a virtual environment**

   - **Windows**

      ```bash
      python -m venv .venv
      .venv\bin\Activate.ps1
      ```

   - **Linux/macOS/Termux**
      ```bash
      python -m venv .venv
      source .venv/bin/activate
      ```

3. **Installing [requirements.txt](./requirements.txt)**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create an app on `Spotify for developer` and get:**

   - Client ID
   - Client secret
   - Redirect URI (example: `http://127.0.0.1:8888/callback`)

5. **Create a `.env` file in the root with these variables:**
    ```env
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    ```

6. **You can change the path of the directory where you download the songs**
    ```py
    DOWNLOAD_PATH = Path.home() / "my_spotify_song"
    ```

## 📋 How to run 

```bash
python main.py
```

## 📜 License

**This project is licensed under the terms of the [Wu Zhoupeng License 1.0](./LICENSE.md)**

## ⚠️ Disclaimer

**THIS PROJECT IS PROVIDED FOR EDUCATIONAL PURPOSES ONLY. USING IT TO DOWNLOAD COPYRIGHTED CONTENT WITHOUT PERMISSION MAY VIOLATE THE TERMS OF SERVICE OF SPOTIFY, YOUTUBE OR OTHER PLATFORMS, AS WELL AS COPYRIGHT LAWS. THE AUTHOR ASSUMES NO RESPONSIBILITY FOR ANY MISUSE OF THIS SCRIPT**