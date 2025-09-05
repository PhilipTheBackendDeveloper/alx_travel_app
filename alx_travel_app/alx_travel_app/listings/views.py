from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def hello_world(request):
    return JsonResponse({"message": "Welcome to ALX Travel App!"})


# listings/views.py


@api_view(['GET'])
def sample_listings(request):
    """
    A simple sample endpoint to test Swagger.
    """
    data = {
        "message": "Welcome to ALX Travel App Listings!",
        "status": "success"
    }
    return Response(data)
