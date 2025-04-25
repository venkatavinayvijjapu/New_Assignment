from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from news_aggregator_tool import NewsAggregatorTool
from analyzer import *

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

web_search_tool = SerperDevTool()
web_scraper_tool = ScrapeWebsiteTool()
content_analyzer_tool = ContentAnalysisTool()
news_aggregator_tool = NewsAggregatorTool()
