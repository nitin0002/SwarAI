import openai
from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

def analyze_response(user_input: str) -> str:
    """
    Analyze the user response and generate an appropriate follow-up question or feedback.
    Uses the GPT-4-turbo model via OpenAI API.
    """
    prompt = f"""
You are an AI cold caller. Analyze the following user response and generate a follow-up question or corrective feedback.
User Response: "{user_input}"
AI Response:"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=100,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()
