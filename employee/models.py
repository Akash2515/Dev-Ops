"""This models will act as a orm for the application"""
from django.db import models



# Create your models here.
class Roles(models.Model):
    """This class creats the roles"""
    RoleId = models.AutoField(primary_key=True)
    RoleNm = models.CharField(max_length=200)

class Project(models.Model):
    """This class creats the Project roles"""
    ProjectId = models.AutoField(primary_key=True)
    ProjectNm = models.CharField(max_length=200)

class Employee(models.Model):
    """This class creats the employee timesheet"""
    Id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True)
    emp_name = models.CharField(max_length=255)
    date_time_in = models.CharField(max_length=255)
    date_time_out = models.CharField(max_length=255)
    duration = models.FloatField()
    # hourly_rate = models.FloatField()
    is_approved = models.BooleanField(default=False)
    # RoleId =models.ForeignKey(Roles,on_delete=models.CASCADE)
    ProjectId = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
