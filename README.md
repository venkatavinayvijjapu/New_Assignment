
# 🧠 CrewAI Blog Research Agent

This project uses the **CrewAI framework** to create a multi-agent system that performs web research, content scraping, analysis, and writing assistance for blog/article generation. It includes custom tools like a **Web Scraper**, **Content Analyzer**, and **News Aggregator** to streamline the research workflow.

---

## 🚀 Features

- 🔍 Web Search Tool using Serper.dev
- 🌐 Web Scraper for extracting content from URLs
- 🗞️ News Aggregator using NewsAPI
- 📊 Content Analysis using Gemini (Google Generative AI)
- 🧑‍💻 Autonomous agents for researching and writing
- ⚙️ Built on [CrewAI](https://github.com/joaomdmoura/crewAI)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/venkatavinayvijjapu/crew-ai-blog-agent.git
cd crew-ai-blog-agent
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

Add a `.env` file in the root directory with the following keys:

```env
SERPER_API_KEY=your_serper_api_key
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_google_generative_ai_key
```

---

## 🧪 Tools Overview

### 🔎 Web Search Tool
Uses Serper.dev to search the web for a given topic.

### 🌐 Web Scraper Tool
Extracts text content from any public webpage.

### 🗞️ News Aggregator Tool
Fetches the latest 5 news articles related to a topic using NewsAPI.

### 📊 Content Analysis Tool
Analyzes content for **sentiment**, **key topics**, and **bias** using Gemini.

---

## 🧠 Agent Roles

- **Research Agent**: Uses tools to gather insights and sources.
- **Writer Agent**: Composes summaries or article drafts based on the research.

---

## ▶️ Running the Agent

To run the entire system:

```bash
python crew.py
```

The agents will collaborate to fetch, analyze, and write content based on your topic prompt.

---

## 📂 Project Structure

```
├── agents.py
├── analyzer.py
├── crew.py
├── tasks.py
├── tools.py
├── web_search_tool.py
├── web_scraper_tool.py
├── news_aggregator_tool.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📋 Requirements

- Python 3.9+
- CrewAI
- Google Generative AI SDK
- Serper.dev API key
- NewsAPI key

---

## 📬 Contact

For help or feedback, feel free to open an issue or reach out via email[venkatavinayvijjapu@gmail.com].

