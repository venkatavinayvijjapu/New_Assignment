from crewai import Task
from agents import research_agent, writer_agent
from tools import web_search_tool, web_scraper_tool, content_analyzer_tool, news_aggregator_tool

research_task = Task(
    description=(
        "Analyze the query '{topic}', break it down into sub-topics, perform web search, scrape content,"
        " analyze and synthesize information to produce a structured summary with references."
    ),
    expected_output="Detailed findings with summarized insights, data points, and key resources used.",
    tools=[web_search_tool, web_scraper_tool, content_analyzer_tool, news_aggregator_tool],
    agent=research_agent
)

write_task = Task(
    description=(
        "Using the analyzed research on '{topic}', generate a well-structured markdown report."
        " Include sections such as Introduction, Key Findings, News Highlights, Conflicting Info (if any),"
        " and a final Summary."
    ),
    expected_output="Markdown report file including key findings, structured sections, and readable formatting.",
    tools=[content_analyzer_tool],
    agent=writer_agent,
    output_file="web_research_report.md"
)