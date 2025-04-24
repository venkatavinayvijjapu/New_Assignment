from typing import Any, Dict, Optional
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Extra
from langchain_core.tools import BaseTool
import requests

class ContentAnalyzerAPIWrapper(BaseModel):
    api_url: str = "http://127.0.0.1:8000"

    class Config:
        extra = Extra.forbid

    def _analyze(self, text: str) -> str:
        response = requests.post(f"{self.api_url}/analyze_content", json={"text": text})
        if response.status_code == 200:
            return response.json().get("analysis", "No analysis returned")
        else:
            return "Content analysis failed"

    def run(self, text: str) -> str:
        return self._analyze(text)


class ContentAnalyzerTool(BaseTool):
    name: str = "content_analyzer_tool"
    description: str = (
        "Analyzes a block of text for key points, summaries, or sentiment. "
        "Input should be plain text."
    )
    api_wrapper: ContentAnalyzerAPIWrapper

    def _run(self, text: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return self.api_wrapper.run(text)
