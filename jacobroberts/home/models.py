from django.db import models

# Create your models here.
class Experience(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=250)