from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(max_length=50, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    createat = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.CharField(max_length=50, blank=True, default='')
    gpa = models.FloatField(null=True, blank=True, default='0.0')
    release_date = models.DateTimeField(auto_now_add=True)
