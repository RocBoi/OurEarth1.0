import requests

def download_file(url, filepath):

    response = requests.get(url, stream=True)

    with open(filepath, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

    return filepath
