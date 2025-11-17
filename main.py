from fastapi import FastAPI
from database import init_pool

import routes

app = FastAPI()


@app.on_event("startup")
async def startup():
    init_pool


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
