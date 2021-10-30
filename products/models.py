from django.db import models
from django.db.models.deletion import SET_NULL
from django.core.validators import FileExtensionValidator

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="brand_images", null=True)

    def __str__(self):
        return str(self.brand_name)

class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_images")

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True)
    image = models.ManyToManyField(ProductImage, blank=True)
    obj = models.FileField(upload_to='product_obj', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['obj'])])
