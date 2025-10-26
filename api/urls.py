from django.urls import path
from .views import root, hello_api

urlpatterns = [
    path('', root),          # http://127.0.0.1:8000/api/
    path('hello/', hello_api) # http://127.0.0.1:8000/api/hello/
]
