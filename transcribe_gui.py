import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import os
import threading

audio_paths = []  # List of selected audio files

def choose_files():
    global audio_paths
    paths = filedialog.askopenfilenames(
        title="Select Audio Files",
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac"), ("All Files", "*.*")]
    )
    if paths:
        audio_paths = list(paths)
        file_label.config(text=f"{len(audio_paths)} files selected")
        transcribe_button.config(state=tk.NORMAL)

def run_transcriptions():
    if not audio_paths:
        messagebox.showwarning("No files", "Please choose audio files.")
        return

    transcribe_button.config(state=tk.DISABLED)
    status_label.config(text=f"⏳ Transcribing {len(audio_paths)} files... Please wait")

    def worker():
        try:
            model = whisper.load_model("base")  # Load model once

            for idx, path in enumerate(audio_paths, start=1):
                status_label.config(text=f"⏳ Transcribing file {idx}/{len(audio_paths)}: {os.path.basename(path)}")
                result = model.transcribe(path)
                srt_text = to_srt(result["segments"])

                default_name = os.path.splitext(os.path.basename(path))[0] + ".srt"
                srt_path = filedialog.asksaveasfilename(
                    title=f"Save transcript for {os.path.basename(path)}",
                    defaultextension=".srt",
                    initialfile=default_name,
                    filetypes=[("SubRip Subtitle", "*.srt")]
                )
                if srt_path:
                    with open(srt_path, "w", encoding="utf-8") as f:
                        f.write(srt_text)
                else:
                    # User canceled saving this file
                    pass

            status_label.config(text="✅ All transcriptions done!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            status_label.config(text="❌ Transcription failed.")
        finally:
            transcribe_button.config(state=tk.NORMAL)

    threading.Thread(target=worker).start()

def to_srt(segments):
    srt = ""
    for i, segment in enumerate(segments, start=1):
        start = format_timestamp(segment["start"])
        end = format_timestamp(segment["end"])
        text = segment["text"].strip()
        srt += f"{i}\n{start} --> {end}\n{text}\n\n"
    return srt

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# GUI Setup
root = tk.Tk()
root.title("Audio to Subtitle (SRT) Transcriber")
root.geometry("500x250")

choose_button = tk.Button(root, text="Choose Audio Files", command=choose_files)
choose_button.pack(pady=10)

file_label = tk.Label(root, text="No files selected")
file_label.pack(pady=5)

transcribe_button = tk.Button(root, text="Transcribe to SRT", command=run_transcriptions, state=tk.DISABLED)
transcribe_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
