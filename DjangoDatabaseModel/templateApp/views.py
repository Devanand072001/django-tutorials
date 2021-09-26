from django.shortcuts import render
from django.http import HttpResponse
from DbApp.models import Employee

def displayDetails(request):
    # return HttpResponse('<h1> This is application</h1> ')
    emp_data = Employee.objects.all()
    # print(emp_data)
    emp_dict = {'emp_list': emp_data}
    dict = { 1 : 'one' , 2 : 'two', 3: 'three'}
    return render(request, 'index.html', context = dict)
# Create your views here.
