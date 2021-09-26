from django.shortcuts import render
from django.http import HttpResponse, request
from datetime import datetime

def display_time(request):
    current_time = datetime.now()
    return HttpResponse('Current time is: '+ str(current_time))

# Create your views here.
