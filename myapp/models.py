from django.db import models

# Create your models here.

class Student(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(unique=True,blank=False)
    password=models.CharField(max_length=30,blank=False)
    contacts=models.CharField(max_length=30,blank=False)
    profile_pic=models.FileField(upload_to="img",default="default.jpg")
    otp=models.IntegerField(default=456)

class Newsletter(models.Model):
    email=models.EmailField(unique=True)

class Blog(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=False, auto_now_add=False)
    pic=models.FileField(upload_to="img",default="default.jpg")