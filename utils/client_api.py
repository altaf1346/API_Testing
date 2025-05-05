import requests
import logging

logging.basicConfig(level=logging.INFO)

class Api:
    Base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.Base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            return response
        except requests.RequestException as e:
            logging.error(f"Error making GET request to {url}: {e}")
            raise

    def post(self, endpoint, data):
        url = f"{self.Base_url}/{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            return response
        except requests.RequestException as e:
            logging.error(f"Error making GET request to {url}: {e}")
            raise

    def put(self, endpoint, data):
        url = f"{self.Base_url}/{endpoint}"
        try:
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            return response
        except requests.RequestException as e:
            logging.error(f"Error making GET request to {url}: {e}")
            raise

    
    def delete(self, endpoint):
        url = f"{self.Base_url}/{endpoint}"
        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            return response
        except requests.RequestException as e:
            logging.error(f"Error making GET request to {url}: {e}")
            raise