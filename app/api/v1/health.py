from fastapi import APIRouter

from app.models.response import ApiResponse

router = APIRouter()


@router.get("/health", response_model=ApiResponse)
async def health():

    return ApiResponse(
        success=True,
        message="Application is healthy",
        data={
            "status": "Running"
        }
    )