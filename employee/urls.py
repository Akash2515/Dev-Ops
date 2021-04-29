"""This urls.py wiil be used for path of the website"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees', views.employees, name='employees')
]
