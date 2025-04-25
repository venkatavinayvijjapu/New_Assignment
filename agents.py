from crewai import Agent, LLM
from tools import web_search_tool, web_scraper_tool, content_analyzer_tool, news_aggregator_tool
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-1.5-flash",
    verbose=True,
    temperature=0.5
)

research_agent = Agent(
    role="Web Research Analyst",
    goal="Perform comprehensive research on {topic} using web tools, and generate accurate and structured findings.",
    verbose=True,
    memory=True,
    backstory=(
        "An expert at gathering and analyzing information from the web, this agent is capable of handling diverse query types,"
        " synthesizing data, resolving conflicts, and presenting information in an organized and useful format."
    ),
    tools=[web_search_tool, web_scraper_tool, content_analyzer_tool, news_aggregator_tool],
    llm=llm,
    allow_delegation=True
)

writer_agent = Agent(
    role="Research Report Writer",
    goal="Generate clear, concise, and structured research reports on {topic} based on provided findings.",
    verbose=True,
    memory=True,
    backstory=(
        "This agent excels at presenting complex research in an accessible format. It crafts summaries, highlights important data,"
        " and ensures reports are informative and reader-friendly."
    ),
    tools=[content_analyzer_tool],
    llm=llm,
    allow_delegation=False
)
