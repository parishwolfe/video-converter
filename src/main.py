#!/usr/bin/env python3

import os
import sys
import argparse
import mimetypes
from moviepy.editor import *

# Function to convert the input video file to MP4 format
def convert_to_mp4(input_file, output_file):
    # Check if the input file is a video
    file_type, _ = mimetypes.guess_type(input_file)
    if not file_type or not file_type.startswith('video'):
        print(f"Skipped {input_file}: Not a video file")
        return False

    # Load the input file as a video clip
    clip = VideoFileClip(input_file)

    # Write the video clip to the output file in MP4 format
    clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

    # Log the successful conversion
    print(f"Converted {input_file} to {output_file}")

    # Return True to indicate a successful conversion
    return True

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Convert video files to MP4 and move to target folder.")
    parser.add_argument("input_folder", help="Path to the input folder")
    parser.add_argument("output_folder", help="Path to the output folder")
    parser.add_argument("--output-log", help="Path to the output log file", default=None)
    parser.add_argument("--input-log", help="Path to the input log file", default=None)
    args = parser.parse_args()

    # Check if input folder exists
    if not os.path.exists(args.input_folder):
        print(f"Input folder '{args.input_folder}' does not exist.")
        sys.exit(1)

    # Create output folder if it doesn't exist
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Read input log file and store paths in a set
    input_log = set()
    if args.input_log and os.path.exists(args.input_log):
        with open(args.input_log, "r") as f:
            for line in f:
                input_log.add(line.strip())

    # Define supported video file extensions
    supported_extensions = ('.avi', '.mkv', '.flv', '.mov', '.mpg', '.wmv', '.mp4')

    # Open output log file if specified
    if args.output_log:
        output_log = open(args.output_log, "a")
    else:
        output_log = None

    # Walk through the input folder and process video files
    for root, dirs, files in os.walk(args.input_folder):
        for file in files:
            # Check if the file has a supported video file extension
            if file.lower().endswith(supported_extensions):
                input_file = os.path.join(root, file)
                # Skip file if it's listed in the input log
                if input_file in input_log:
                    print(f"Skipping {input_file} as it's listed in the input log.")
                    continue
                # Convert the video and save it to the output folder
                output_file = os.path.join(args.output_folder, os.path.splitext(file)[0] + '.mp4')
                success = convert_to_mp4(input_file, output_file)
                # Log the successfully converted file to the output log
                if success and output_log:
                    output_log.write(f"{input_file}\n")

    # Close the output log file if it's open
    if output_log:
        output_log.close()

if __name__ == "__main__":
    main()
