from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=15)
    city=models.CharField(max_length=15)