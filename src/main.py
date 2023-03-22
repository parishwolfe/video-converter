#!/usr/bin/env python3

import os
import sys
import argparse
from moviepy.editor import *

def convert_to_mp4(input_file, output_file):
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"Converted {input_file} to {output_file}")
        return True
    except Exception as e:
        print(f"Error converting {input_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert video files to MP4 and move to target folder.")
    parser.add_argument("input_folder", help="Path to the input folder")
    parser.add_argument("output_folder", help="Path to the output folder")
    parser.add_argument("--output-log", help="Path to the output log file", default=None)
    parser.add_argument("--input-log", help="Path to the input log file", default=None)
    args = parser.parse_args()

    if not os.path.exists(args.input_folder):
        print(f"Input folder '{args.input_folder}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    input_log = set()
    if args.input_log and os.path.exists(args.input_log):
        with open(args.input_log, "r") as f:
            for line in f:
                input_log.add(line.strip())

    supported_extensions = ('.avi', '.mkv', '.flv', '.mov', '.mpg', '.wmv', '.mp4')

    if args.output_log:
        output_log = open(args.output_log, "a")
    else:
        output_log = None

    for root, dirs, files in os.walk(args.input_folder):
        for file in files:
            if file.lower().endswith(supported_extensions):
                input_file = os.path.join(root, file)
                if input_file in input_log:
                    print(f"Skipping {input_file} as it's listed in the input log.")
                    continue
                output_file = os.path.join(args.output_folder, os.path.splitext(file)[0] + '.mp4')
                success = convert_to_mp4(input_file, output_file)
                if success and output_log:
                    output_log.write(f"{input_file}\n")

    if output_log:
        output_log.close()

if __name__ == "__main__":
    main()
