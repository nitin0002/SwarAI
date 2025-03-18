import os
from google.cloud import texttospeech
from app.config import Config

def generate_speech(text: str, filename: str = "output.mp3") -> str:
    """
    Generate speech audio from the given text using Google Cloud Text-to-Speech.
    """
    # Set credentials for Google Cloud TTS
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Config.GOOGLE_APPLICATION_CREDENTIALS
    
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice_params,
        audio_config=audio_config
    )
    
    with open(filename, "wb") as out:
        out.write(response.audio_content)
    
    return filename
