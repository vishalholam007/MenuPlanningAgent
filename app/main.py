from fastapi import FastAPI

from app.config.settings import settings
from app.config.logging import logger
from app.middleware.exception_handler import global_exception_handler

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)


@app.on_event("startup")
async def startup():

    logger.info("======================================")
    logger.info("Menu Planning Agent Started")
    logger.info("======================================")


@app.get("/")
async def home():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "Healthy"
    }