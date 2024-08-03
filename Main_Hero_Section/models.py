from django.db import models

# Create your models here.

class Main_Hero_Section(models.Model):
    title_1 = models.CharField(max_length=60)
    title_2 = models.CharField(max_length=60,null=True)
    description = models.TextField(max_length=300)
    price = models.CharField(max_length=60)
    image= models.FileField(max_length=200 , upload_to="Main_Hero_Section/", null=True)