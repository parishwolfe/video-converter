import unittest
import os
import tempfile
import shutil
from moviepy.editor import *
import sys

# Add the 'src' directory to the system path to import 'video_converter'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import convert_to_mp4

class TestVideoConverter(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_convert_to_mp4_success(self):
        # Create a short video for testing
        test_video_path = os.path.join(self.test_dir, 'test_video.avi')
        clip = ColorClip((320, 240), color=(255, 0, 0), duration=1)
        clip.fps = 24
        clip.write_videofile(test_video_path, codec='png', audio_codec=None)

        # Convert the test video to MP4
        output_video_path = os.path.join(self.test_dir, 'test_video.mp4')
        result = convert_to_mp4(test_video_path, output_video_path)

        # Check if the conversion was successful
        self.assertTrue(result)

        # Check if the output MP4 file exists
        self.assertTrue(os.path.exists(output_video_path))

    def test_convert_to_mp4_failure(self):
        # Create a non-video file for testing
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('This is a test file.')

        # Try converting the test file to MP4
        output_video_path = os.path.join(self.test_dir, 'test_video.mp4')
        result = convert_to_mp4(test_file_path, output_video_path)

        # Check if the conversion failed
        self.assertFalse(result)

        # Check if the output MP4 file does not exist
        self.assertFalse(os.path.exists(output_video_path))

if __name__ == '__main__':
    unittest.main()
