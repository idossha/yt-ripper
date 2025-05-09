# YouTube MP3 Downloader

A simple Python script to download YouTube videos as high-quality MP3 files from a list of URLs.

## Features

- Downloads YouTube videos as MP3 files (320kbps quality)
- Processes multiple URLs from a text file
- Creates timestamped download directories
- Shows download progress and summary
- Simple command-line interface

## Requirements

- Python 3.6 or higher
- yt-dlp
- FFmpeg (for audio conversion)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/yt-ripper.git
cd yt-ripper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)

## Usage

1. Create a text file (e.g., `urls.txt`) with YouTube URLs, one per line:
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
```

2. Run the script:
```bash
python youtube_downloader.py urls.txt
```

The script will:
- Create a new directory in `downloads/mp3_TIMESTAMP/`
- Download each video as a 320kbps MP3 file
- Show progress for each download
- Display a summary when complete

## Output

Files are saved in the `downloads` directory with timestamps:
```
downloads/
└── mp3_20240321_123456/
    ├── video_title_1.mp3
    ├── video_title_2.mp3
    └── ...
```

## License

MIT License
