# api_utils.py
import requests

def fetch_data(url):
    """
    Fetches data from an API endpoint.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def post_data(url, data):
    """
    Posts data to an API endpoint.
    """
    response = requests.post(url, json=data)
    return response.status_code == 201

def put_data(url, data):
    """
    Puts data to an API endpoint.
    """
    response = requests.put(url, json=data)
    return response.status_code == 200
