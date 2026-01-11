import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_gemini(model, prompt, system_prompt):
    llm = genai.GenerativeModel(model,system_instruction=system_prompt)
    response = llm.generate_content(prompt)
    return response.text
