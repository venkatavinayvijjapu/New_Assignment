from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")

router = APIRouter()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

class AnalyzeRequest(BaseModel):
    content: str

@router.post("/analyze_content")
async def analyze_content(request: AnalyzeRequest):
    prompt = (
        "Analyze the following content for sentiment, key topics, and any biased language. "
        "Return it in JSON format with keys: sentiment, topics, and bias:\n\n"
        f"{request.content}"
    )
    response = model.generate_content(prompt)
    return {"analysis": response.text}
