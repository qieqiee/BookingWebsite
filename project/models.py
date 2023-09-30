from django.db import models

# Create your models here.
class Student (models.Model):
    studentid = models.CharField(max_length=10,primary_key=True)
    studentname = models.TextField(max_length=100)
    studentphone = models.TextField(max_length=15)

class Felo (models.Model):
    feloid = models.CharField(max_length=10,primary_key=True)
    password = models.TextField(max_length=8)


class Washingmachine (models.Model):
    machineNo = models.CharField(max_length=5,primary_key=True)
    machineType = models.TextField(max_length=50)
    machineLocation = models.TextField(max_length=50)

class Book (models.Model): 
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    machineNo = models.ForeignKey(Washingmachine, on_delete=models.CASCADE)
    laundrydate = models.DateField(blank=True,null=True)
    starttime = models.TimeField(blank=True,null=True)
    endtime = models.TimeField(blank=True,null=True)