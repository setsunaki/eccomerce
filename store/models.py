from distutils.command.upload import upload
from pyexpat import model
from unicodedata import category
from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.ImageField()
    images = models.ImageField(upload_to ='photos/products')
    stock = models.ImageField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name