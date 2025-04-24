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

class NewsTopicRequest(BaseModel):
    topic: str

@router.post("/news_summary")
async def fetch_news_summary(data: NewsTopicRequest):
    prompt = (
        f"Provide a concise news summary (3-4 bullet points) on the current topic: {data.topic}. "
        "Include sources if possible."
    )
    response = model.generate_content(prompt)
    return {"news_summary": response.text}
