import imp
from operator import mod
from statistics import mode
from django.db import models
from account.models import User
from category.models import Courses,Teacher
# Create your models here.

class Shopping(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Courses,on_delete=models.CASCADE)
    total_price = models.IntegerField()
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
