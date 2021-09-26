from django.shortcuts import render
from django.http import HttpResponse, request
def greeting(request):
    return HttpResponse('<h1> Hello <h1>')
# Create your views here.
