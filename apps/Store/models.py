from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# from .views import category_list
# category table 

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    # data about data
    class Meta:
        verbose_name_plural = "categories" 
    
    def get_absolute_url(self):
       return reverse('Store:category_list', args=[self.slug])
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creater')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description  =models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)  # - for desc

    def get_absolute_url(self): 
        return reverse("Store:product_details", kwargs={"slug": self.slug})
    

    # save image as same size for all 

    # def save(self, *args, **kwargs):
    #     self.image = Image.open(self.image.path).resize((400,300), Image.ANTIALIAS)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
# from PIL import Image


def __str__(self):
    return self.title

