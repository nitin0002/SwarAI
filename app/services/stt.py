import whisper

# Load the Whisper model once at startup
model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe the audio file using Whisper.
    """
    result = model.transcribe(audio_path)
    return result["text"]
