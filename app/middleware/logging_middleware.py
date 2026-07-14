import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.config.logging import logger
from app.utils.request_id import generate_request_id


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = generate_request_id()

        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        logger.info(
            f"[{request_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration}s"
        )

        response.headers["X-Request-ID"] = request_id

        return response