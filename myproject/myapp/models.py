from django.db import models
from decimal import Decimal


class Users(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Address=models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    Age=models.IntegerField()
    Password=models.CharField(max_length=50)
    Cpassword=models.CharField(max_length=50)

class Products(models.Model):
    Image=models.ImageField(upload_to='myproject/myapp/static/images')
    Name=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)


class Cart(models.Model):
    Image = models.FileField(upload_to='myproject\myapp\static\images')
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.IntegerField(default=0)