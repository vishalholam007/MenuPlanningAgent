from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.config.logging import logger
from app.config.settings import settings
from app.middleware.exception_handler import global_exception_handler
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    logger.info("Application Started")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Application Stopped")