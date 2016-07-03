from django.shortcuts import render
from models import Employee, User, Student
from django.http import HttpResponse
# Create your views here.

def create(request):
    user = User.objects.create(
        email="pedro.kong@company.com",
        first_name="Pedro",
        last_name="Kong"
        
    )
    employee = Employee(employee_id="123", designation="Maths Professor")
    user.employees.append(employee)
    user.save()
    return HttpResponse("Employee created")

'''
def employee(request):
    employee = Employee.objects.create(
        email="pedro.kong@company.com",
        first_name="Pedro",
        last_name="Kong"
    )
    employee.employee_id = "123"
    employee.designation = "Maths Professor"
    employee.save()
    return HttpResponse("Employee created")
'''