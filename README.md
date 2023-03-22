# Video Converter

Video Converter is a command-line utility that walks through a target file system, finds video files with specific extensions, and converts them to MP4 format. The converted files are then placed in a specified output folder. The utility also supports input and output log files. Input log files contain a list of file paths that should be skipped during processing, while output log files store the paths of successfully converted files.

## Getting Started

Follow these steps to set up and run the Video Converter utility:

Prerequisites

- Python 3.6 or higher
- MoviePy library

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/video-converter.git
cd video-converter
```

Set up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
.\venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the utility with the following command:

```bash
python src/main.py /path/to/input/folder /path/to/output/folder --input-log input_log.txt --output-log output_log.txt
```

Replace /path/to/input/folder and /path/to/output/folder with the appropriate input and output folder paths. The --input-log and --output-log arguments are optional.

## Running Tests

To run the unit tests, navigate to the tests directory and execute the test_main.py script:

```bash
cd tests
python test_main.py
```

The tests will run and report the results.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

MoviePy - A Python library for video editing.
