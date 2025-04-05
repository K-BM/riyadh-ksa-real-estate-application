import requests
import json 
from config.api_config import BASE_URL, ENDPOINTS
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key securely from environment variables
API_KEY = os.getenv("API_KEY")

# Function to make POST requests to API endpoints
def fetch_data(endpoint, data):
    url = f"{BASE_URL}{ENDPOINTS[endpoint]}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None