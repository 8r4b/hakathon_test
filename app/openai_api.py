import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_diagnosis_from_openai(symptoms: str) -> str:
    """
    Send symptoms to OpenAI and return the AI-generated diagnosis or suggestion.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": f"Given these symptoms, what is a possible diagnosis or advice? Symptoms: {symptoms}"}
            ],
            max_tokens=150,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error contacting OpenAI: {e}"