from django.shortcuts import render
from django.http import HttpResponse

def one(request):
    return HttpResponse('<h1> test view one </h1>')

def two(request):
    return HttpResponse('<h1> test view two </h1>')

def three(request):
    return HttpResponse('<h1> test view three </h1>')
# Create your views here.
