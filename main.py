from fastapi import FastAPI
from database import create_pool

import routes

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.pool = await create_pool()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    routes.score_detection_router, prefix=f"/api/{
        routes.score_detection_route_prefix}"
)


@app.on_event("shutdown")
async def shutdown():
    app.state.pool.close()
    await app.state.pool.wait_closed()
