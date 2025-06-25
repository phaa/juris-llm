from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from logging_config import logger
from rag.embed_chunks import generate_data_store
from api import main

logger.info(f"Initializing ChromaDB")
generate_data_store()

logger.info("Initializing FastAPI")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

# Prometheus middleware endpoint /metrics
Instrumentator().instrument(app).expose(app)

logger.info("Initializing Routes")
app.include_router(main.router, prefix="", tags=["index"])