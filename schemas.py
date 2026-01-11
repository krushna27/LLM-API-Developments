from pydantic import BaseModel

class LLMRequest(BaseModel):
    provider: str   # openai, gemini, groq, hf, mistral
    model: str
    prompt: str
    system_prompt: str = ""
