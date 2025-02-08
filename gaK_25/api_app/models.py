from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    archieved = models.BooleanField()