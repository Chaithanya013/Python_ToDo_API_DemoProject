from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def root(request):
    return Response({"message": "Welcome to the API root!"})

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello from Django API!"})

