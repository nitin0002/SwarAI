from fastapi import APIRouter, BackgroundTasks, UploadFile, File
from app.services import tts, voip, stt, ai_analysis

router = APIRouter()

@router.post("/call")
async def start_call(phone_number: str, background_tasks: BackgroundTasks):
    """
    Initiate a call to the provided phone number.
    Generates the first question using TTS and initiates the VoIP call.
    """
    first_question = "Hello! What is your name?"
    # Generate TTS audio for the initial question
    audio_file = tts.generate_speech(first_question, filename="question.mp3")
    
    # Use Linphone-based call (or swap out with voip.make_twilio_call for Twilio)
    background_tasks.add_task(voip.make_call, phone_number, audio_file)
    
    return {"status": "Call initiated"}

@router.post("/response")
async def handle_response(user_audio: UploadFile = File(...)):
    """
    Process the recorded user audio response.
    Transcribe the audio, analyze it, and generate a follow-up response.
    """
    # Save the uploaded audio to a temporary file
    temp_path = f"temp/{user_audio.filename}"
    with open(temp_path, "wb") as f:
        content = await user_audio.read()
        f.write(content)
    
    # Transcribe the audio using Whisper
    user_text = stt.transcribe_audio(temp_path)
    
    # Analyze the user response with an AI model
    ai_reply = ai_analysis.analyze_response(user_text)
    
    # Generate TTS audio for the AI's reply
    audio_reply_file = tts.generate_speech(ai_reply, filename="ai_reply.mp3")
    
    # (Optional) Save call log to the database using models.call_log here
    
    return {"ai_response": ai_reply, "audio_reply_file": audio_reply_file}
