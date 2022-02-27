from django.contrib import admin

# Register your models here.
from .models import Product, ProductMedia


admin.site.register(Product)
admin.site.register(ProductMedia)