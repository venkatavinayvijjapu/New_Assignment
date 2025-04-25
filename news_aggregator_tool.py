import os
import requests
from typing import Any, Optional, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class NewsAggregatorToolSchema(BaseModel):
    """Input schema for NewsAggregatorTool."""
    topic: str = Field(..., description="Topic to search recent news articles about")


class NewsAggregatorTool(BaseTool):
    name: str = "News Aggregator Tool"
    description: str = "Fetches the latest news articles related to a given topic using NewsAPI."
    args_schema: Type[BaseModel] = NewsAggregatorToolSchema

    def _run(self, topic: str) -> str:
        api_key = os.getenv("NEWS_API_KEY")
        if not api_key:
            return "Error: NEWS_API_KEY environment variable not set."

        url = "https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 5,
            "apiKey": api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            articles = response.json().get("articles", [])

            if not articles:
                return f"No recent news articles found for the topic: {topic}."

            news_summary = f"📰 Latest news articles about **{topic}**:\n\n"
            for article in articles:
                title = article.get("title", "No title")
                source = article.get("source", {}).get("name", "Unknown source")
                url = article.get("url", "")
                news_summary += f"- {title} ({source})\n  {url}\n"

            return news_summary

        except requests.exceptions.RequestException as e:
            return f"An error occurred while fetching news articles: {e}"
