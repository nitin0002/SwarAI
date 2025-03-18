from pydantic import BaseModel
from datetime import datetime

class CallLog(BaseModel):
    id: int = None  # To be assigned by the database
    phone_number: str
    transcript: str
    ai_response: str
    timestamp: datetime = datetime.now()
