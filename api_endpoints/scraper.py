from fastapi import APIRouter
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/scrape_url")
async def scrape_url(data: URLRequest):
    try:
        res = requests.get(data.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        text = soup.get_text()
        return {"scraped_text": text[:1000]}  # Return first 1000 chars
    except Exception as e:
        return {"error": str(e)}
