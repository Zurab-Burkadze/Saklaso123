from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=100)
    publish_date = models.DateField()
    archieved = models.BooleanField()
    write_date = models.DateTimeField()