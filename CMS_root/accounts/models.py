from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="demo.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    CATAGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    catagory = models.CharField(max_length=200, null=True, choices=CATAGORY)
    descriprion = models.CharField(max_length=500 ,null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Canceled Order','Canceled Order'),
        ('Delivered','Delivered')
        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    statur = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200, null=True)
    order_content = models.DecimalField(max_digits= 10000, null=True, decimal_places=0)


    def __str__(self):
        return str(self.customer)