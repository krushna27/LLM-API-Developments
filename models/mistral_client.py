import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Initializing Hugging Face TOKEN
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def generate_mistral(model, system_prompt, user_prompt):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    res = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
        json=payload
    )
    return res.json()["choices"][0]["message"]["content"]
