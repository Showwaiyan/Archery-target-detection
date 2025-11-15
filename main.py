from fastapi import FastAPI

import routes

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(
    routes.score_detection_router, prefix=routes.score_detection_route_prefix
)
