"""This urls.py wiil be used for path of the website"""
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('userdashboard', views.userdashboard, name='userdashboard'),
    path('approvalprocessing', views.approvalprocessing, name='approvalprocessing')

]
