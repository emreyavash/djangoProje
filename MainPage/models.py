from django.db import models

# Create your models here.

class About(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description =models.TextField()