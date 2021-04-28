"""This view.py will help to perform backend works """
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee

def index(request):
    """This method will retur the home page """
    return render(request, 'index.html')


def employees(request):
    """this method will do the updateing the employer db"""
    if request.method == 'POST' :
        emp_id = request.POST['emp_id']
        emp_name = request.POST['emp_name']
        project_id = request.POST['ProjectId']
        date_time_in = request.POST['date_time_in']
        date_time_out = request.POST['date_time_out']
        duration = request.POST['duration']
        # hourly_rate = request.POST['hourly_rate']
        employee = Employee(emp_id=emp_id,
            emp_name=emp_name,
            ProjectId_id =project_id,
            date_time_in=date_time_in,
            date_time_out=date_time_out,
            duration=duration)
        employee.save()
        messages.success(request, 'Time Sheet added successfully')
        return redirect('/roles/userdashboard')

def testcallback():
    """ this method will return success """
    return 'success'
