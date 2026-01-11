import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_openai(model, prompt, system_prompt):
    res = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt},
                  {"role":"system","content": system_prompt}]
    )
    return res.choices[0].message.content
