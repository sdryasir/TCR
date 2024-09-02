from django.db import models

# Create your models here.
class CARS(models.Model):
    name = models.CharField(max_length=60,null=True)
    image= models.FileField(max_length=200 , upload_to="Cars/", null=True)
    new_car = models.CharField(max_length=60,null=True,blank=True)
    category = models.CharField(max_length=60,null=True,blank=True)
    passengers = models.CharField(max_length=60,null=True)
    stock = models.IntegerField(null=True)
    price = models.CharField(max_length=60,null=True)  
    petrol_diesel = models.CharField(max_length=60,null=True,blank=True)
    automatic_manual = models.CharField(max_length=60,null=True,blank=True)
    at_mt = models.CharField(max_length=60,null=True,blank=True)
    car_image_1= models.FileField(max_length=200 , upload_to="Cars/", null=True,blank=True)
    car_image_2= models.FileField(max_length=200 , upload_to="Cars/", null=True,blank=True)
    car_image_3= models.FileField(max_length=200 , upload_to="Cars/", null=True,blank=True)
    car_image_4= models.FileField(max_length=200 , upload_to="Cars/", null=True,blank=True)
    rating_per = models.CharField(max_length=60,null=True,blank=True)
    reviews = models.CharField(max_length=60,null=True,blank=True)
    description = models.TextField(max_length=300,blank=True)  
    feature_1 = models.CharField(max_length=60,null=True,blank=True)
    feature_2 = models.CharField(max_length=60,null=True,blank=True)
    feature_3 = models.CharField(max_length=60,null=True,blank=True)
    feature_4 = models.CharField(max_length=60,null=True,blank=True)
    feature_5 = models.CharField(max_length=60,null=True,blank=True)
    feature_6 = models.CharField(max_length=60,null=True,blank=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Our Cars"  # Plural name (same as singular, to avoid pluralization)