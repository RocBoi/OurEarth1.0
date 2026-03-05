from fastapi import FastAPI
from eosdis_client import search_dataset

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Our Earth API online"}

@app.get("/datasets/{dataset}")
def datasets(dataset: str):
    results = search_dataset(dataset)
    return results
