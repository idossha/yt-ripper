
#!python3

import argparse
import yt_dlp

def download_audio(url, output_name):
    # Options for downloading highest quality audio in original format
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio format available
        'outtmpl': output_name,  # Output file name
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract the audio using ffmpeg
            'preferredcodec': 'mp3',  # You can change to mp3 for compression, or leave it original
            'preferredquality': '320',  # Set quality for MP3 to 320 kbps
        }],
        'keepvideo': False  # Download audio only
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Download YouTube videos as high-quality audio files."
    )

    # Add the arguments
    parser.add_argument(
        'url',
        type=str,
        help='The URL of the YouTube video to download audio from.'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='audio.mp3',  # You can change the default extension to match the original format (e.g., '.opus' or '.m4a')
        help='The name of the output file (default: audio.mp3).'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to download the audio
    download_audio(args.url, args.output)

if __name__ == '__main__':
    main()
