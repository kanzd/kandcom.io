from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=20,default="")
    catagory=models.CharField(max_length=20,default="")
    subcatagory = models.CharField(max_length=20,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300,default="")
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images")
    def __str__(self):
        return self.product_name
class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    pascode=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class cart(models.Model):
    id=models.AutoField
    products=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    payment=models.BooleanField()
    def __str__(self):
        return self.email
class pcart(models.Model):
    id=models.AutoField
    products=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    payment=models.BooleanField()
    def __str__(self):
        return self.email
