# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    # Add code for get requests to back end
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(backend_url + endpoint, params=kwargs)
        # Check if the request was successful
        response.raise_for_status()
        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # If any error occurs during the request
        print(f"Network exception occurred: {e}")
        return None

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

def post_review(data_dict):
    # Add code for posting review
    try:
        # Call post method of requests library with URL and data
        response = requests.post(backend_url + "/insert_review", json=data_dict)
        # Check if the request was successful
        response.raise_for_status()
        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # If any error occurs during the request
        print(f"Network exception occurred: {e}")
        return None
