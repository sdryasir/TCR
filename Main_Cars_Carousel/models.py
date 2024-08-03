from django.db import models

# Create your models here.
class Main_Cars_Carousel(models.Model):
    image= models.FileField(max_length=200 , upload_to="Main_Cars_Carousel/", null=True)