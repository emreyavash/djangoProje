
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
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

class Teacher(models.Model):
    teacherName = models.CharField(max_length=150)
    teacherDescription = models.CharField(max_length=150,null=True)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    def __str__(self) :
        return f"{self.teacherName}"
    def save(self,*args, **kwargs):
        self.slug = slugify(self.teacherName)
        super().save(*args, **kwargs)

class Courses(models.Model):
    courseName =models.CharField(max_length=150)
    is_active=models.BooleanField(default=False)
    is_home =models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    coursePrice = models.IntegerField()
    numberOfStudent = models.IntegerField()
    category = models.ManyToManyField(Category)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=150,default="")
    courseImage= models.ImageField(upload_to="courses",null=True)
    def __str__(self) :
        return f"{self.courseName}"
    def save(self,*args, **kwargs):
        self.slug = slugify(self.courseName)
        super().save(*args, **kwargs)
