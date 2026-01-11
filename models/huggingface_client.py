import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Initializing Hugging Face TOKEN
HF_API = os.getenv("HF_API_KEY")

def generate_hf(model, prompt):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {HF_API}"}

    payload = {"inputs": prompt}

    res = requests.post(url, headers=headers, json=payload)
    data = res.json()
    return data[0]["generated_text"]
