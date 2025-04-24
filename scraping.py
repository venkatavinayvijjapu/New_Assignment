from typing import Any, Dict, Optional
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Extra
from langchain_core.tools import BaseTool
import requests

class WebScraperAPIWrapper(BaseModel):
    api_url: str = "http://127.0.0.1:8000"

    class Config:
        extra = Extra.forbid

    def _scrape(self, url: str) -> str:
        response = requests.post(f"{self.api_url}/scrape_url", json={"url": url})
        if response.status_code == 200:
            return response.json().get("content", "No content found")
        else:
            return "Failed to scrape URL"

    def run(self, url: str) -> str:
        return self._scrape(url)


class WebScraperTool(BaseTool):
    name: str = "web_scraper_tool"
    description: str = (
        "Scrapes the textual content of a given URL. "
        "Input should be a valid URL."
    )
    api_wrapper: WebScraperAPIWrapper

    def _run(self, url: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return self.api_wrapper.run(url)
