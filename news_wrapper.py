from typing import Any, Dict, Optional
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Extra
from langchain_core.tools import BaseTool
import requests

class NewsAggregatorAPIWrapper(BaseModel):
    api_url: str = "http://127.0.0.1:8000"

    class Config:
        extra = Extra.forbid

    def _get_news(self, topic: str) -> str:
        response = requests.post(f"{self.api_url}/news", json={"topic": topic})
        if response.status_code == 200:
            return response.json().get("articles", "No news found")
        else:
            return "News fetching failed"

    def run(self, topic: str) -> str:
        return self._get_news(topic)


class NewsAggregatorTool(BaseTool):
    name: str = "news_aggregator_tool"
    description: str = (
        "Fetches the latest news articles on a given topic. "
        "Input should be a topic like 'AI', 'sports', or 'economy'."
    )
    api_wrapper: NewsAggregatorAPIWrapper

    def _run(self, topic: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return self.api_wrapper.run(topic)
