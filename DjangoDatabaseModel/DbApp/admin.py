from django.contrib import admin
from DbApp.models import Employee 

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin ):
    emp_details = ['emp_no', 'emp_name', 'emp_salary', 'emp_email']
admin.site.register(Employee)
