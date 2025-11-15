from fastapi import APIRouter, UploadFile
from controllers.score_detection_controller import save_target_file

tag = "scores-detaction"
router_prefix = "/arrowStaging"
router = APIRouter(tags=[tag])


@router.post("/detect", tags=[tag])
async def create_detection(file: UploadFile):
    return await save_target_file(file)
