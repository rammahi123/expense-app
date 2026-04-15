from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logger
import logging

setup_logger()
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
def startup_event():
    logger.info("Starting Expense API...")

@app.get("/health")
def health_check():
    logger.info("Health check triggered")
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": settings.APP_NAME}
