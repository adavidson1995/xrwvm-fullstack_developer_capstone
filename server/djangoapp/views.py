# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from . import restapis


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)  # Logs the user out
    data = {"userName": ""}
    return JsonResponse(data)  # Returns a JSON response as required

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "/fetchDealers"
        # Get dealers from the URL
        dealerships = restapis.get_request(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer["short_name"] for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        url = f"/fetchReviews/dealer/{dealer_id}"
        # Get reviews from the URL
        reviews = restapis.get_request(url)
        if reviews is not None:
            # Return the reviews as JSON
            return JsonResponse(reviews, safe=False)
        else:
            return JsonResponse({"error": "Reviews not found"}, status=404)

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        url = f"/fetchDealer/{dealer_id}"
        # Get dealer details from the URL
        dealer_details = restapis.get_request(url)
        if dealer_details:
            # Return the first dealer details (since it's a list)
            return JsonResponse(dealer_details[0])
        else:
            return JsonResponse({"error": "Dealer not found"}, status=404)

# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        # Get the review data from the request
        data = json.loads(request.body)
        # Post the review to the backend
        result = restapis.post_review(data)
        if result:
            return JsonResponse({"status": "success", "message": "Review added successfully"})
        else:
            return JsonResponse({"status": "error", "message": "Failed to add review"}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
