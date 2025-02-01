from django.db import models

class Saklaso(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    edited = models.BooleanField(default=False)
    write_date = models.DateTimeField()
