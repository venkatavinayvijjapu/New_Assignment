import os
from typing import Any
import google.generativeai as genai
from dotenv import load_dotenv
from crewai.tools import BaseTool
from pydantic import PrivateAttr


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


class ContentAnalysisTool(BaseTool):
    name: str = "Content Analysis Tool"
    description: str = "Analyzes content for sentiment, key topics, and potential biases."

    _model: Any = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    def _run(self, content: str) -> str:
        if not content:
            return "Error: No content provided for analysis."

        prompt = (
            "Analyze the following content for sentiment, key topics, and any biased language. "
            "Return it in JSON format with keys: sentiment, topics, and bias:\n\n"
            f"{content}"
        )

        try:
            response = self._model.generate_content(prompt)
            return self._format_response(response.text)
        except Exception as e:
            return f"An error occurred during content analysis: {e}"

    def _format_response(self, response_text: str) -> str:
        try:
            analysis = eval(response_text)
        except Exception as e:
            return f"Failed to parse model response: {e}"

        sentiment = analysis.get("sentiment", "Not found")
        topics = analysis.get("topics", "Not found")
        bias = analysis.get("bias", "Not found")

        return (
            f"Sentiment: {sentiment}\n"
            f"Key Topics: {topics}\n"
            f"Bias: {bias}"
        )
