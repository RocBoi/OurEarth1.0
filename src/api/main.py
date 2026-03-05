from fastapi import FastAPI
from atmosphere_api import router as atmosphere_router

app = FastAPI()

app.include_router(atmosphere_router)

@app.get("/")
def root():
    return {"message": "Our Earth API online"}
