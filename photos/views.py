from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Location,Category,Image

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')