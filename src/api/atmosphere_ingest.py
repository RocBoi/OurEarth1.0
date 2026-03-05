import os
import requests
from datetime import datetime

DATA_DIR = "data/raw"

os.makedirs(DATA_DIR, exist_ok=True)

def download_dataset(url, filename):

    path = os.path.join(DATA_DIR, filename)

    response = requests.get(url, stream=True)

    if response.status_code == 200:

        with open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        return {"status": "downloaded", "file": path}

    return {"error": "download failed"}

def fetch_sample_atmosphere():

    dataset_url = "https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/A2023001.L3m_DAY_AER_AEROSOL_4km.nc"

    today = datetime.utcnow().strftime("%Y%m%d")

    filename = f"atmosphere_{today}.nc"

    return download_dataset(dataset_url, filename)


if __name__ == "__main__":

    result = fetch_sample_atmosphere()

    print(result)
