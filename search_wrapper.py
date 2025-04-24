from typing import Any, Dict, Optional
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Extra
from langchain_core.tools import BaseTool
import requests

class WebSearchAPIWrapper(BaseModel):
    """Wrapper for Web Search API."""
    
    api_url: str = "http://127.0.0.1:8000"  # Change as per your deployment

    class Config:
        extra = Extra.forbid

    def _web_search(self, query: str) -> str:
        response = requests.post(f"{self.api_url}/web_search", json={"query": query})
        if response.status_code == 200:
            return response.json().get("result", "No result returned")
        else:
            return "Web search failed"

    def run(self, query: str) -> str:
        return self._web_search(query)


class WebSearchTool(BaseTool):
    name: str = "web_search_tool"
    description: str = (
        "A tool for performing live web search. "
        "Useful for answering questions about recent events or retrieving web content. "
        "Input should be a search query."
    )
    api_wrapper: WebSearchAPIWrapper

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return self.api_wrapper.run(query)
