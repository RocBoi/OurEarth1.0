import requests

EOSDIS_SEARCH_URL = "https://cmr.earthdata.nasa.gov/search/granules.json"

def search_dataset(dataset):

    params = {
        "short_name": dataset,
        "page_size": 5
    }

    response = requests.get(EOSDIS_SEARCH_URL, params=params)

    if response.status_code == 200:
        return response.json()

    return {"error": "dataset not found"}
