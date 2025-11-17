from fastapi import APIRouter, UploadFile
from pydantic import BaseModel, field_validator
from typing import List, Any
from controllers.score_detection_controller import (
    detect_target_file,
    insert_arrows_to_staging,
)


class ArrowStagingPayload(BaseModel):
    roundID: int
    participationID: int
    distance: str
    endOrder: int
    arrows: List[Any]

    @field_validator("roundID", "participationID", "endOrder")
    def must_be_positive(cls, v, info):
        if v <= 0:
            raise ValueError(f"{info.name} must be a positive integer.")
        return v

    @field_validator("arrows")
    def arrows_not_empty(cls, v):
        if not v:
            raise ValueError("arrows list cannot be empty.")
        return v


tag = "scores-detaction"
router_prefix = "archer"
router = APIRouter(tags=[tag])


@router.post("/arrows", tags=[tag])
async def create_ends(payload: ArrowStagingPayload):
    return await insert_arrows_to_staging(payload)


@router.post("/{range_id}/detect", tags=[tag])
async def create_detection(file: UploadFile, range_id: int):
    return await detect_target_file(file, range_id)
