# Audio to SRT Transcription Application

## Overview

This is a **simple graphical desktop application** built with Python that allows you to convert audio files into subtitle files (`.srt`) with **automatically generated, time-synced captions** and **perfect punctuation**.

The application uses **OpenAI’s Whisper speech recognition model** to transcribe spoken words from audio files accurately. It generates subtitle files that you can use for videos, presentations, or any content requiring captions.

---

## What does this application do?

- **Loads any audio file** (MP3, WAV, etc.) from any folder on your computer.
- Uses advanced **speech-to-text AI** (Whisper) to transcribe the spoken words.
- Automatically **adds punctuation** to make the text readable and natural.
- Splits the transcript into **time-coded subtitle segments** following the SRT format.
- Allows you to **choose the output folder** to save the `.srt` subtitle file.
- Provides an easy-to-use **Graphical User Interface (GUI)** — just select the input audio file, pick where you want to save the captions, and click “Transcribe” to start.
- Shows progress and completion status for convenience.

---

## Why use this?

- **Save time** manually typing subtitles for your videos or audio content.
- **Improve accessibility** by adding captions with accurate timing.
- Work offline with your own files — no need to upload sensitive audio anywhere.
- Get **punctuated, clean transcripts** that are ready to use right away.

---

## How does it work?

1. You open the app and click **“Select Audio”** to pick your audio file anywhere on your computer.
2. Then click **“Select Save Folder”** to choose where the subtitle file will be saved.
3. Press **“Transcribe”** and the app uses Whisper to process the audio and generate the transcript with punctuation.
4. The output is saved as an `.srt` file — a standard subtitle format that works with most video players and editors.
5. You can then use this `.srt` file alongside your video or audio for captions.

---

## How to use

### Prerequisites:
- Python 3.8 or higher installed.
- `ffmpeg` installed and added to your system PATH (required by Whisper).
- Python packages installed: `whisper`, `torch`, `ffmpeg-python`, `tkinter` (usually built-in with Python).

### Running the app:
1. Clone or download this repository.
2. Open a terminal/command prompt in the project folder.
3. Install requirements (if not done yet):

### Install OpenAi Whisper:
```bash
1. pip install openai-whisper torch ffmpeg-python
2. Run the GUI app:

bash
Copy
Edit
python transcribe_gui.py
Use the interface to select your audio file, choose a save location, and transcribe.

### Supported Files:
Supported audio formats
- .mp3

- .wav

- .m4a

- .flac

and others supported by FFmpeg.


### Output
Output
- .srt subtitle file with time-coded captions.

File saved in the folder you specify, named after your audio file.

Troubleshooting
Make sure ffmpeg is installed and added to your system’s PATH.

Large audio files may take some time to transcribe depending on your computer.

Use supported audio file formats to avoid errors.

License
MIT License

Additional Notes
The transcription process uses OpenAI's Whisper model for speech recognition, which provides highly accurate transcriptions with proper punctuation.

Ensure that your audio file path and save folder path are accessible and correctly selected in the GUI.

This application is designed to work offline; no audio or text is uploaded to any external server.

For best results, use clear audio recordings with minimal background noise.

If you have any questions or run into issues, please feel free to open an issue in the repository or contact me directly.
