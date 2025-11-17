from fastapi import APIRouter, UploadFile
from controllers.score_detection_controller import detect_target_file

tag = "scores-detaction"
router_prefix = "arrowStaging"
router = APIRouter(tags=[tag])


@router.post("/{range_id}/detect", tags=[tag])
async def create_detection(file: UploadFile, range_id: int):
    return await detect_target_file(file, range_id)
