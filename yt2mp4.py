#!python3 

import argparse
import yt_dlp

def download_video(url, output_name):
    # Options for downloading MP4 video
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Best video + audio in MP4 format
        'outtmpl': output_name,  # Output file name
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Download YouTube videos as MP4 files."
    )

    # Add the arguments
    parser.add_argument(
        'url',
        type=str,
        help='The URL of the YouTube video to download.'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='video.mp4',
        help='The name of the output file (default: video.mp4).'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to download the video
    download_video(args.url, args.output)

if __name__ == '__main__':
    main()
