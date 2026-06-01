import requests

def fetch_data(url):
    response = requests.get(url, timeout=10)
    return response.json()
