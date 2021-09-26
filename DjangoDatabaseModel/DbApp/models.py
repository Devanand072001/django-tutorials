from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_no = models.IntegerField()
    emp_name= models.CharField(max_length = 20)
    emp_salary = models.IntegerField()
    emp_email = models.CharField(max_length=30)

# create sql query
# python manage.py makemigrations 
# python manage.py makemigrations DbApp

# execute sql query
# python manage.py migrate

# create table
# python manage.py sqlmigrate DbApp 0001