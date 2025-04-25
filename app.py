import streamlit as st
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_groq import ChatGroq

from search_wrapper import WebSearchAPIWrapper
from scraping import WebScraperAPIWrapper
from news_wrapper import NewsAggregatorAPIWrapper
from contentwrapper import ContentAnalyzerAPIWrapper
from prompt import * # Custom prompt for web research tasks
from gpt_utils import *
import os
from dotenv import load_dotenv


load_dotenv() 

api_key = os.getenv("GROQ_API_KEY")
st.set_page_config(page_title="Web Research Agent", layout="wide")
st.title("🕵️ Web Research AI Agent")

# -------------------- Initialize Wrappers --------------------

if "web_tool" not in st.session_state:
    st.session_state.web_tool = web_search_tool()

if "scraper_tool" not in st.session_state:
    st.session_state.scraper_tool = scraper_tool()

if "news_tool" not in st.session_state:
    st.session_state.news_tool = news_aggregator_tool()

if "analyzer_tool" not in st.session_state:
    st.session_state.analyzer_tool = content_analyzer_tool()

# -------------------- Initialize Agent --------------------

if "prompt" not in st.session_state:
    st.session_state.prompt = get_prompt()
    print(st.session_state.prompt)

if "agent_executor" not in st.session_state:
    llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile", api_key=api_key)
    tools = [
        st.session_state.web_tool,
        st.session_state.scraper_tool,
        st.session_state.news_tool,
        st.session_state.analyzer_tool,
    ]
    agent = create_openai_tools_agent(llm, tools, st.session_state.prompt)
    st.session_state.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# -------------------- Chat Interface --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# New user query input
if user_input := st.chat_input("Ask your Web Research question here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Let me investigate..."):
        response = st.session_state.agent_executor.invoke({"input": user_input})
        output = response["output"]
        st.session_state.messages.append({"role": "assistant", "content": output})
        with st.chat_message("assistant"):
            st.markdown(output)
