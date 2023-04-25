from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=500,default="",null=True,blank=True)
    image = models.ImageField(upload_to="upload/products/")

    def __str__(self) :
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self) :
        return self.first_name

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50 , default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    # def __str__(self) :
    #     return self.customer