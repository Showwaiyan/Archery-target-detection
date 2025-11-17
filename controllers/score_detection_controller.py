from fastapi import UploadFile, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from os import getenv, makedirs, remove

from services.score_detection_services import (
    get_detection_result,
    unpack_detection_target,
)

load_dotenv()


async def save_target_file(file: UploadFile, range_id: int):
    # Create dir
    UPLOAD_DIR = getenv("UPLOAD_DIR")
    makedirs(UPLOAD_DIR, exist_ok=True)
    file_location = f"{UPLOAD_DIR}/{range_id}.jpeg"
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    result = await get_detection_result(file_location)
    target, scores = await unpack_detection_target(result)

    remove(file_location)

    if target is None and scores is None:
        raise HTTPException(
            status_code=500,
            detail="Sorry, We cannot find your current range information",
        )

    if target is None:
        raise HTTPException(
            status_code=400,
            detail="Target is not detected, Please take a photo in other direction or different lighting",
        )

    result = jsonable_encoder(scores)
    return JSONResponse(content=scores)
