from django.db import models

# Create your models here.
class Add_Your_Car_Section(models.Model):
    title_line_1 = models.CharField(max_length=100,null=True,blank=True)
    title_line_2 = models.CharField(max_length=100,null=True,blank=True)
    des_line_1 = models.CharField(max_length=100,null=True,blank=True)
    des_line_2 = models.CharField(max_length=100,null=True,blank=True)
    add_car_button = models.CharField(max_length=60,null=True,blank=True)
    background_image= models.FileField(max_length=200 , upload_to="Add_Your_Car_Section/", null=True,blank=True)
    mobile_background_image= models.FileField(max_length=200 , upload_to="Add_Your_Car_Section/", null=True,blank=True)


    
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Add Your Car Section"  # Plural name (same as singular, to avoid pluralization)