from fastapi import FastAPI
from database import init_pool
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from os import getenv

import routes

load_dotenv()

app = FastAPI()

origins = [getenv("REACT_URL")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await init_pool()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    routes.score_detection_router, prefix=f"/api/{
        routes.score_detection_route_prefix}"
)


@app.on_event("shutdown")
async def shutdown():
    from database import pool
    pool.close()
    await pool.wait_closed()
