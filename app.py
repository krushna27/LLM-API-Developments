DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant. Answer clearly, concisely, and correctly. and in short sentences."


from fastapi import FastAPI, HTTPException
from schemas import LLMRequest

from models.openai_client import generate_openai
from models.gemini_client import generate_gemini
from models.groq_client import generate_groq
from models.huggingface_client import generate_hf
from models.mistral_client import generate_mistral
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI(title="Multi LLM API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],        # Allow OPTIONS, POST, GET, etc.
    allow_headers=["*"],
)


@app.post("/generate")
def generate_text(request: LLMRequest):

    system_prompt = request.system_prompt or DEFAULT_SYSTEM_PROMPT


    if request.provider == "openai":
        return {"response": generate_openai(request.model, system_prompt, request.prompt)}

    elif request.provider == "gemini":
        return {"response": generate_gemini(request.model, system_prompt, request.prompt)}

    elif request.provider == "groq":
        return {"response": generate_groq(request.model, system_prompt, request.prompt)}

    elif request.provider == "hf":
        return {"response": generate_hf(request.model, system_prompt, request.prompt)}

    elif request.provider == "mistral":
        return {"response": generate_mistral(request.model, system_prompt, request.prompt)}

    else:
        raise HTTPException(status_code=400, detail="Invalid provider")
