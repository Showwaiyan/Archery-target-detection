from fastapi import APIRouter

tag = "scores-detaction"
router_prefix = "/scores-detection"
router = APIRouter(tags=[tag])


@router.get("/", tags=[tag])
async def create_detection():
    return {"message": "Hello Detection"}
