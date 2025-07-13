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
----
# 🗣️ Transcription Application

A simple desktop GUI app that converts audio files into subtitle files (`.srt`) with **highly accurate transcriptions and proper punctuation** using OpenAI’s Whisper model.

---

## ✅ Installation

Install the required Python packages:

---

## 🚀 How to Run the GUI App



Then:

- Select your **audio file**
- Choose a **save location** for the `.srt` subtitle file
- Click **Transcribe** and wait — transcription will start automatically

---

## 🎵 Supported Audio Formats

- `.mp3`
- `.wav`
- `.m4a`
- `.flac`
- ...and other formats supported by **FFmpeg**

---

## 📝 Output

- Generates a `.srt` subtitle file with **time-coded captions**
- Output file is saved in the folder you selected, using the audio filename

---

## 🛠 Troubleshooting

- ✅ Make sure `ffmpeg` is installed and added to your system’s **PATH**
- 🕐 Long audio files may take a few minutes to process depending on your system
- 🎧 Use **clear audio** for best results
- 📂 Ensure audio and save folders are accessible

---

## 🔐 License

MIT License

---

## 📌 Additional Notes

- The app uses **OpenAI Whisper** for transcription
- Works **100% offline** — no internet or external API needed
- Great for podcasts, sermons, interviews, YouTube videos, etc.
- Produces transcriptions with **accurate punctuation**
- User-friendly GUI — no command line needed once it's running

---

## 🚧 Future Enhancements

### 1. 🎧 Multiple File Batch Processing
- Select and transcribe multiple audio files at once
- Each file will generate its own `.srt` automatically

### 2. 📊 Progress Bar & Status Updates
- Show real-time progress and estimated time remaining

### 3. 🔉 Audio Preview & Playback
- Built-in audio player with synced caption preview

### 4. 🌍 Language Selection
- Let users select audio language for better recognition

### 5. 🗂 Output Format Options
- Export to `.srt`, `.vtt`, `.txt`, or `.json`

### 6. 📝 Editable Transcript Editor
- View and edit transcripts before saving

### 7. ⏱ Timestamp Customization
- Adjust subtitle timing, delay, or segment size

### 8. 🌙 Dark Mode / UI Themes
- Light/dark mode toggle for better visibility

### 9. 🖱 Drag & Drop Support
- Drag audio files directly into the app window

### 10. 🕓 Save Recent Files / History
- Keep history of recent transcripts for fast access

### 11. 🏷 Automatic Filename Suggestions
- Smart naming based on file metadata or time

### 12. 🔄 Audio Format Conversion
- Auto-convert unsupported formats using FFmpeg

### 13. 💻 Desktop Executable Packaging
- Package as standalone `.exe`, `.app`, or `.deb` using PyInstaller

---

💬 **Have suggestions or issues?**  
Open an issue or submit a pull request. Contributions are welcome!



## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software for personal or commercial use, provided that the original license is included.

Read the full license [here](LICENSE).


