from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from os import getenv, makedirs

load_dotenv()


async def save_target_file(file: UploadFile, archer_id: int):
    # Create dir
    UPLOAD_DIR = getenv("UPLOAD_DIR")
    makedirs(UPLOAD_DIR, exist_ok=True)
    file_location = f"{UPLOAD_DIR}/{archer_id}.jpeg"
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    return JSONResponse(content=True)
