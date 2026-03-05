import os
import xarray as xr
from fastapi import APIRouter

router = APIRouter()

DATA_PATH = "data/raw"

def latest_dataset():

    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".nc")]

    if not files:
        return None

    files.sort(reverse=True)

    return os.path.join(DATA_PATH, files[0])


@router.get("/atmosphere/live")
def live_atmosphere():

    dataset_path = latest_dataset()

    if dataset_path is None:
        return {"error": "no dataset available"}

    ds = xr.open_dataset(dataset_path)

    summary = {}

    for var in ds.data_vars:
        summary[var] = float(ds[var].mean().values)

    return {
        "dataset": dataset_path,
        "variables": summary
    }
