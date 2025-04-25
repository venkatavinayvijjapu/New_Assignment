
# 🕵️ Web Research AI Agent

This project is a **Web Research AI Agent** that integrates multiple tools such as web search, scraping, news summarization, and content analysis using LLMs. Built with **FastAPI**, **Streamlit**, and **LangChain**, this app enables users to ask complex queries and receive intelligent, structured responses.

---

## 🛠️ Features

- 🌐 **Web Search** – Search the web using DuckDuckGo.
- 📰 **News Aggregation** – Fetch and summarize latest news articles.
- 🧠 **Content Analyzer** – Detect sentiment, topics, and bias in text.
- 🔍 **Web Scraper** – Scrape and extract text content from URLs.
- 🧩 **LangChain Integration** – Modular agent with tool-based reasoning.
- 🎨 **Streamlit UI** – Chat-like interface for asking questions.

---

## 📁 Project Structure

```
.
├── api.py                         # FastAPI main backend entry
├── app.py                         # Streamlit frontend app
├── api_endpoints/                # FastAPI endpoints for tools
│   ├── analyze.py
│   ├── news.py
│   ├── scraper.py
│   └── web_search.py
├── contentwrapper.py             # Wrapper and tool for content analysis
├── news_wrapper.py               # Wrapper and tool for news summaries
├── scraping.py                   # Wrapper and tool for scraping URLs
├── search_wrapper.py             # Wrapper and tool for web search
├── gpt_utils.py                  # Tool setup for agent
├── prompt.py                     # LangChain hub prompt loader
├── .env                          # Environment variables
└── requirements.txt              # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/venkatavinayvijjapu/New_Assignment.git
cd web-research-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.9 or later.

### 3. Setup Environment Variables

Create a `.env` file in the root directory and add the following:

```env
GEMINI_API_KEY=your_google_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 🧪 Running the Project

### 1. Start the FastAPI Backend

```bash
uvicorn api:app --reload
```

This will run the FastAPI server at `http://127.0.0.1:8000`

You can test endpoints like:

- `POST /analyze_content`
- `POST /web_search`
- `POST /scrape_url`
- `POST /news_summary`

### 2. Launch the Streamlit Frontend

Open a new terminal window and run:

```bash
streamlit run app.py
```

This starts the frontend interface at `http://localhost:8501`.

---

## 🧭 Flow of Execution

1. **Streamlit UI (`app.py`)** is loaded and tools are initialized:
   - Web Search Tool
   - Scraper Tool
   - News Aggregator Tool
   - Content Analyzer Tool

2. **User inputs a question** in the chat interface.

3. **LangChain Agent** is created using:
   - `create_openai_tools_agent` from LangChain
   - LLM: `llama-3.3-70b-versatile` via GROQ API

4. **Agent parses the query**, selects the relevant tool(s) and invokes the backend API using:
   - `requests` calls defined in wrapper classes

5. **FastAPI Endpoint** processes the request (e.g. fetches data, analyzes text using Gemini API, scrapes web pages).

6. **Response is returned** to the user as a markdown message in the chat.

---

## 🔐 API Integration Details

- **Google Gemini API** – Used in `analyze.py` for content analysis.
- **GROQ LLM API** – Used via `ChatGroq` to power the LangChain agent.

---

## 🧪 Example Usage

- “Summarize recent news about electric vehicles.”
- “Scrape this article and analyze it for bias: https://example.com/article”
- “Search the web for the latest on quantum computing.”
- “Analyze this paragraph for sentiment.”

---

## 📈 Metrics

The backend is instrumented using `prometheus_fastapi_instrumentator`. Visit `/metrics` on the FastAPI server to see real-time metrics.

