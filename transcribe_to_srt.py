import whisper

def transcribe_audio_to_srt(audio_file_path, model_size='medium'):
    model = whisper.load_model(model_size)

    print("⏳ Transcribing... This may take a few minutes, especially for long audio.")
    result = model.transcribe(audio_file_path)

    srt_lines = []
    for i, segment in enumerate(result['segments']):
        def format_time(seconds):
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            millis = int((seconds - int(seconds)) * 1000)
            return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

        start = format_time(segment['start'])
        end = format_time(segment['end'])
        text = segment['text'].strip()

        srt_lines.append(f"{i+1}")
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(f"{text}\n")

    with open("transcript_output.srt", "w", encoding="utf-8") as f:
        f.write('\n'.join(srt_lines))

    print("✅ Transcription complete!")
    print("📁 File saved as: transcript_output.srt")

if __name__ == "__main__":
    # 🔁 Change the file name below to match your 33-minute audio file
    audio_file = "voice1.mp3"  # Example: sermon.mp3
    transcribe_audio_to_srt(audio_file)
#yes sir