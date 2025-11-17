from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from typing import List, Any
from controllers.score_detection_controller import detect_target_file, update_ends_scores


class ArrowStagingPayload(BaseModel):
    roundID: int
    participationID: int
    distance: int
    target: int
    endOrder: int
    arrows: List[Any]


tag = "scores-detaction"
router_prefix = "arrowStaging"
router = APIRouter(tags=[tag])


@router.post("/{archer_id}/detect", tag=[tag])
async def post_ends_scores(archer_id: int, payload: ArrowStagingPayload):
    return await update_ends_scores(archer_id, payload)


@router.post("/{range_id}/detect", tags=[tag])
async def create_detection(file: UploadFile, range_id: int):
    return await detect_target_file(file, range_id)
