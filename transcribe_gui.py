import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import os
import threading

audio_path = None  # Store selected audio file path

def choose_file():
    global audio_path
    path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac"), ("All Files", "*.*")]
    )
    if path:
        audio_path = path
        file_label.config(text=os.path.basename(audio_path))
        transcribe_button.config(state=tk.NORMAL)

def run_transcription():
    if not audio_path:
        messagebox.showwarning("No file", "Please choose an audio file.")
        return

    transcribe_button.config(state=tk.DISABLED)
    status_label.config(text="⏳ Transcribing... please wait")

    def worker():
        try:
            model = whisper.load_model("base")  # Change to "small" or "medium" if need
            result = model.transcribe(audio_path)
            srt_text = to_srt(result["segments"])

            # Ask user where to save the SRT file
            default_name = os.path.splitext(os.path.basename(audio_path))[0] + ".srt"
            srt_path = filedialog.asksaveasfilename(
                title="Save Transcript As",
                defaultextension=".srt",
                initialfile=default_name,
                filetypes=[("SubRip Subtitle", "*.srt")]
            )

            if srt_path:
                with open(srt_path, "w", encoding="utf-8") as f:
                    f.write(srt_text)
                status_label.config(text=f"✅ Done! Saved as:\n{srt_path}")
            else:
                status_label.config(text="⚠️ Transcription done, but save was canceled.")
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

choose_button = tk.Button(root, text="Choose Audio File", command=choose_file)
choose_button.pack(pady=10)

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=5)

transcribe_button = tk.Button(root, text="Transcribe to SRT", command=run_transcription, state=tk.DISABLED)
transcribe_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
