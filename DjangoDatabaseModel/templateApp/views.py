from django.shortcuts import render
from django.http import HttpResponse
from DbApp.models import Employee
# import datetime as time


def displayDetails(request):
    # return HttpResponse('<h1> This is application</h1> ')
    name = "Devanand V"
    emp_data = Employee.objects.all()
    emp_dict = {"emp_list": emp_data}
    return render(request, 'index.html', context = emp_dict)
# Create your views here.
