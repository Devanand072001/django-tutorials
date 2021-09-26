from django.shortcuts import render
from django.http import HttpResponse, request

def greetings_moring(request):
    return HttpResponse('<h1> Good morning </h1>')


def greetings_afternoon(request):
    return HttpResponse('<h1> Good afternoon </h1>')


def greetings_evening(request):
    return HttpResponse('<h1> Good evening </h1>')
# Create your views here.
