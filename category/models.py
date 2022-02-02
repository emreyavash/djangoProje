from msilib.schema import Class
from statistics import mode
from unicodedata import category
from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    is_active= models.BooleanField(default=False)
    categoryImage=models.ImageField()
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    def __str__(self) :
        return f"{self.categoryName}"
    def save(self,*args, **kwargs):
        self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)