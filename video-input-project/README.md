# Video Input Project

## Overview
This project is designed to analyze the sentiment of text extracted from video files. It utilizes the VADER sentiment analysis tool to provide sentiment scores and labels based on the input text.

## Files
- `src/analyzer.py`: Contains the `SentimentAnalyzer` class for sentiment analysis.
- `src/video_input.py`: Handles user input for video files, including prompting for file paths and validating input.
- `src/utils/__init__.py`: Initializes the `utils` package for shared utility functions.
- `requirements.txt`: Lists the dependencies required for the project.

## Setup
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the `video_input.py` script to input a video file.
2. The script will extract text from the video and analyze its sentiment using the `SentimentAnalyzer` class.

## License
This project is licensed under the MIT License.