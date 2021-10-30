from django.contrib import admin

# Register your models here.
from .models import ProductImage, Product, Brand

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Brand)