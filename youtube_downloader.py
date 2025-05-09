#!/usr/bin/env python3

import argparse
import os
import yt_dlp
from datetime import datetime

def download_mp3(url, output_dir):
    """Download video as MP3"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("✓ Download completed!")
            return True
    except Exception as e:
        print(f"✗ Error downloading {url}: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Download YouTube videos as MP3')
    parser.add_argument('urls_file', help='Text file containing YouTube URLs (one per line)')
    
    args = parser.parse_args()
    
    # Create output directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join('downloads', f'mp3_{timestamp}')
    os.makedirs(output_dir, exist_ok=True)
    
    # Read URLs from file
    try:
        with open(args.urls_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{args.urls_file}' not found!")
        exit(1)
    
    print(f"Found {len(urls)} URLs to download")
    
    # Download each video
    successful = 0
    failed = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing...")
        if download_mp3(url, output_dir):
            successful += 1
        else:
            failed += 1
    
    print(f"\nDownload Summary:")
    print(f"✓ Successfully downloaded: {successful}")
    print(f"✗ Failed downloads: {failed}")
    print(f"\nFiles saved in: {output_dir}")

if __name__ == '__main__':
    main() 