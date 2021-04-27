"""This view.py will help to perform backend works """
import json as JSON
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from employee.models import Project
from employee.models import Employee
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings

#this method will be connect to the userdashboard.html
def userdashboard(request):
    user_entries=Employee.objects.order_by('-date_time_out').filter(emp_id=request.user.id).all()
    user_project = Project.objects.order_by('ProjectId')
    employeedata = Employee.objects.filter(is_approved=False).all()
    context = {
        'time_entries': user_entries,
        'projects': user_project,
        'employees': employeedata
    }
    return render(request, 'roles/userdashboard.html', context)

#the user can register if he dont have a account
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        user_id = request.POST['employee_id']
        is_superuser=request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email id exists')
                return redirect('register')

            if User.objects.filter(id=user_id).exists():
                messages.error(request, 'A user with same employee id exists')
                return redirect('register')

            user = User.objects.create_user(username=username,
            password=password,
            email=email,
            id=user_id,
            first_name=first_name,
            is_superuser=is_superuser,
            last_name=last_name)
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')

        messages.error(request, 'Passwords do not match')
        return redirect('register')

    return render(request, 'roles/register.html')

#this function helps to login the user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('userdashboard')
        messages.error(request, 'Invalid Credentials')
        return redirect('login')

    return render(request, 'roles/login.html')

#this method will do the logout operation
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect('index')

#this method will do the approval and reject operation
def approvalprocessing(request):
    body = JSON.loads(request.body)
    print(body)
    if(body["status"]== "True" or body["status"]== "False" ):
        employee_safe=Employee.objects.get(Id=body['Id'])
        employee_safe.is_approved = body['status']
        employee_safe.save()
        for i in User.objects.all().filter(id=body['emp_id']):
            print(i.email)
            print(i.username)
            #if the manager accept the timesheet a message will be sent to the employee
            if body["status"]== "True":
                email=EmailMessage(
                    'Time Sheet info',
                    'Hello'+' '+i.username+'.The Manager has approved your Time Sheet.',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[i.email],
                    )
                email.send()
            #if the manager reject the timesheet a message will be sent to the employee
            else:
                email=EmailMessage(
                    'Time Sheet info',
                    'Hello'+' '+i.username+'.The Manager has approved your Time Sheet.',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[i.email],
                    )
                email.send()
        return JsonResponse({'status':'success'})
