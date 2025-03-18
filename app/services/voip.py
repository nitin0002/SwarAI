import subprocess
import os
from app.config import Config
from twilio.rest import Client

def make_call(phone_number: str, audio_file: str):
    """
    Initiate a VoIP call using Linphone CLI and play the provided audio file.
    Ensure that you have configured your Linphone client (e.g., with linphone_config.cfg).
    """
    # Example command to start a call with Linphone; adjust parameters as needed.
    call_command = f"linphonec -c linphone_config.cfg -d 6 call {phone_number}"
    subprocess.run(call_command, shell=True)
    
    # Command to play the audio file in the call
    play_command = f"linphonec play {audio_file}"
    subprocess.run(play_command, shell=True)

def make_twilio_call(phone_number: str, audio_url: str):
    """
    Initiate a call using Twilio's API.
    The audio_url must be publicly accessible.
    """
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=phone_number,
        from_=Config.TWILIO_PHONE_NUMBER,
        url=audio_url
    )
    print(f"Call initiated: {call.sid}")
