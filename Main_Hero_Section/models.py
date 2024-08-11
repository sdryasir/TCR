from django.db import models

# Create your models here.

class Main_Hero_Section(models.Model):
    title_1 = models.CharField(max_length=60,blank=True)
    title_2 = models.CharField(max_length=60,null=True,blank=True)
    description_1 = models.TextField(max_length=300,blank=True)
    description_2 = models.TextField(max_length=300,null=True,blank=True)   
    price = models.CharField(max_length=60,blank=True)
    image= models.FileField(max_length=200 , upload_to="Main_Hero_Section/", null=True,blank=True)

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Main Hero Section"  # Plural name (same as singular, to avoid pluralization)   