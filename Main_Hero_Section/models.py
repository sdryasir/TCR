from django.db import models

# Create your models here.

class Main_Hero_Section(models.Model):
    caption = models.CharField(max_length=60)
    description = models.TextField(max_length=60)
    price = models.CharField(max_length=60)
    image= models.FileField(max_length=200 , upload_to="Main-Hero-Section/", null=True)