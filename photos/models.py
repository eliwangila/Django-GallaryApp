from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
# class Image(models.Model):
#     image = CloudinaryField('image')
#     image_name = models.CharField(max_length=40)
#     description = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE,default='')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')
    