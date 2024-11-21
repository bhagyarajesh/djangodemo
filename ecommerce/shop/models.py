from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to="categories")


    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to="products")
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

