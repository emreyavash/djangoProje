
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
# Create your models here.
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self,email,username,first_name,last_name,password,city,gender,phone,tc,birthday,**other_fields) :
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )
        return self.create_user(email,username,first_name,last_name,password,gender,birthday,tc,phone,city,**other_fields)

    def create_user(self,email,username,first_name,last_name,password,gender,birthday,tc,phone,city,**other_fields):
        user = self.model(email=email,username=username,first_name=first_name,last_name=last_name,gender=gender,birthday=birthday,tc=tc,city_id=city,phone=phone,**other_fields)
        user.set_password(password)
        user.save()
        return user

class City(models.Model):
    cityName=models.CharField(max_length=20)

class User(AbstractUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday = models.DateField(null=False)
    gender = models.BooleanField(null=False)
    tc= models.CharField(max_length=50)
    studentcertificate = models.ImageField(upload_to="studentcertifica",null=False)
    certificateverify = models.BooleanField(default=False)
    city= models.ForeignKey('City',on_delete=models.CASCADE,null=True)
    emailverify = models.BooleanField(default=False)
    phone= models.CharField(max_length=11,null=True)
    phoneverify= models.BooleanField(default=False)
    objects = CustomAccountManager()
    userImage=models.ImageField(upload_to="users/",null=True)

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS = ["email","first_name","last_name","gender","birthday",'tc','phone','city']

    def __str__(self):
        return self.email
