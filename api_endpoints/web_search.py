from fastapi import APIRouter
from pydantic import BaseModel
from duckduckgo_search import DDGS

router = APIRouter()

class SearchQuery(BaseModel):
    query: str
    max_results: int = 5

@router.post("/web_search")
async def search_web(query: SearchQuery):
    try:
        with DDGS() as ddg:
            results = ddg.text(query.query, max_results=query.max_results)
            return {"results": results}
    except Exception as e:
        return {"error": str(e)}
