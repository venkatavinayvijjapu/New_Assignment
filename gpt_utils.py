from search_wrapper import WebSearchAPIWrapper
from langchain_core.tools import Tool
from scraping import WebScraperAPIWrapper
from news_wrapper import NewsAggregatorAPIWrapper
from contentwrapper import ContentAnalyzerAPIWrapper

def web_search_tool():
    web_search = WebSearchAPIWrapper()
    tool = Tool(
        name="Web-Search-Tool",
        description="Useful for performing general web searches to find recent or relevant information from the internet.",
        func=web_search.run
    )
    return tool




def scraper_tool():
    scraper = WebScraperAPIWrapper()
    tool = Tool(
        name="Web-Scraper-Tool",
        description="Used to scrape content from a specific URL. Returns the main content of the page.",
        func=scraper.run
    )
    return tool



def news_aggregator_tool():
    news = NewsAggregatorAPIWrapper()
    tool = Tool(
        name="News-Aggregator-Tool",
        description="Fetches the latest news articles based on a query. Useful for current events and news summaries.",
        func=news.run
    )
    return tool


def content_analyzer_tool():
    analyzer = ContentAnalyzerAPIWrapper()
    tool = Tool(
        name="Content-Analyzer-Tool",
        description="Analyzes and summarizes web page content or text. Useful for understanding key points or topics.",
        func=analyzer.run
    )
    return tool
