from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = RichTextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)



    def __str__(self):
        return self.title  



class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="media")
    image = models.ImageField(upload_to='product')

    def __str__(self) -> str:
        return str(self.id)