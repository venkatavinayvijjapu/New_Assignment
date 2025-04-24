# import sql_api,csv_api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.sessions import SessionMiddleware
import logging
from api_endpoints import analyze,news,scraper,web_search


logging.basicConfig(filename='api.log', filemode='a', level=logging.INFO, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d- %(message)s')
app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the SessionMiddleware to enable session handling
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.include_router(web_search.router, tags=["Web Searching"])
app.include_router(scraper.router, tags=["Scrapping my data"])
app.include_router(analyze.router, tags=["Analyzer"])
app.include_router(news.router, tags=["News"])

