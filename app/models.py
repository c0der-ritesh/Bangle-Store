from django.db import models
from django.contrib.auth.models import User
class UserDetail(models.Model):
    Name = models.CharField(max_length=20)
    #email = models.EmailField(max_length=254)
    #password = models.CharField(max_length=8)
    Address = models.CharField(max_length=100)
    Adress1 = models.CharField(max_length=100)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=10)

class ProductDetail(models.Model):
    pname = models.CharField(max_length=30)
    pdesc = models.CharField(max_length=200)
    price = models.CharField(max_length=9)
class CartDetail(models.Model):
    productname = models.CharField(max_length=30)
    productdesc = models.CharField(max_length=100)
    price = models.FloatField(max_length=20)
    shipprice = models.FloatField(max_length=10)
    Name = models.CharField(max_length=20,null=True)

class OrderDetail(models.Model):
    Name = models.CharField(max_length=30)
    Netprice = models.FloatField(max_length=12)
    Address = models.CharField(max_length=40)
    State = models.CharField(max_length=10)
    City = models.CharField(max_length=15)
    Zip = models.CharField(max_length=10)
    Date = models.CharField(max_length=15,null=True)
