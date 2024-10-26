# Video Audio Extractor

This Python script allows users to extract audio from .mp4 video files and save it as an .mp3 file. It leverages the moviepy library for video/audio processing and tkinter for user interactions, like file selection and displaying messages.

## Features
- Select and extract audio from .mp4 video files.
- Notifies the user upon successful audio extraction.
- Built-in error handling for file selection and processing issues.

## Requirements

- Ensure you have Python 3.6 or higher installed.

## Required libraries include:

- moviepy for video/audio handling.
- tkinter (typically bundled with Python).
- Install moviepy (If tkinter is not installed, refer to the official installation guide).

### Usage Instructions

- Download and Run the Script.
- Save the script as audio_extractor.py.
- Run the following command in the terminal to start:

  ```bash
  Copy code
  python audio_extractor.py

### Select a Video File

- A file dialog will open, prompting you to select a .mp4 file.
- If you select an unsupported file type or skip file selection, an error message will prompt you to select a valid video file.

### Successful Completion:

- Once the audio is extracted, a message box will confirm the successful completion.
- The audio file will be saved as Extracted_audio.mp3 in the same directory as the script.

### Error Handling

The script manages errors as follows:

- File Selection Error: If no file or an unsupported file type is selected, an error message prompts you to select a correct file.
- Processing Error: If there is an issue with reading or processing the video file, an error message displays.
- Unexpected Errors: Other unexpected errors are caught and displayed to the user.

## License
This project is licensed under the MIT License. See the LICENSE file for further details.

### Quick Reference Commands
To set up and run this script:

  ```bash
  Copy code
  # Install moviepy
  pip install moviepy
  
  # Run the script
  python audio_extractor.py

