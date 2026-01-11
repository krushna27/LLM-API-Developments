from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Get the cohere api key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq()

def generate_groq(model, prompt, system_prompt):
    res = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
