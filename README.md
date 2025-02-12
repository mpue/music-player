# Music Player

A simple music player that can play audio files.

## Included Music and Copyright

This music player includes original music composed by me. While I retain the copyright for all included tracks, everyone is allowed to use my music freely, provided that I am credited as the creator of each individual song. This permission extends to both personal and commercial projects, including but not limited to games and videos.

## Features

- Playback of audio files
- Support for formats like MP3, WAV, OGG
- Play, Pause, Stop
- Volume control
- Progress bar
- Playlist support

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the project:**
   ```bash
   python main.py
   ```

## Usage

1. Start the application.
2. Load a file or playlist via the interface.
3. Control playback using the buttons.

## Docker Instructions

1. **Build the Docker image:**
   ```bash
   docker build -t music-player .
   ```
2. **Run the container:**
   ```bash
   docker run -d --name music_player -p 5000:5000 music-player
   ```
3. **Access the application:**
   Open `http://localhost:5000` in your web browser.

## Requirements

- Python 3.8+

## To-Do

- Shuffle and repeat functions
- Equalizer
- Theme support

## License

MIT License

