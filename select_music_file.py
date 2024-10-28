#!/usr/bin/env python3

import os
import random
import sys
from pathlib import Path
import subprocess

def check_directory(directory):
    """Verify directory exists and contains files"""
    path = Path(directory)
    if not path.is_dir():
        print(f"Directory not found: {directory}")
        sys.exit(1)
    
    files = list(path.glob('*'))
    if not files:
        print(f"No files found in {directory}")
        sys.exit(1)
        
    return files

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 select_random_file.py <video/audio directory>")
        sys.exit(1)

    audio_and_video_dir = sys.argv[1]

    # Get list of files from directories
    audio_and_video_files = check_directory(audio_and_video_dir)

    # Select random files
    selected_music = random.choice(audio_and_video_files)

    # Display selected files
    print("Selected files:")
    print(f"Video/Audio File: {selected_music}")

    # Open the file name that was picked
    print(f"Opening the randomly picked file: {selected_music}")
    subprocess.run(['open', selected_music])


if __name__ == "__main__":
    main()

