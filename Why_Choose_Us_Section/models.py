from django.db import models

# Create your models here.
class Why_Choose_Us_Section(models.Model):
    heading = models.CharField(max_length=60,null=True,blank=True)
    description = models.TextField(max_length=300,blank=True)  
    feature_1 = models.CharField(max_length=60,null=True)
    feature_2 = models.CharField(max_length=60,null=True)
    feature_3 = models.CharField(max_length=60,null=True)
    feature_4 = models.CharField(max_length=60,null=True)
    icon_code_1 = models.CharField(max_length=60,null=True,blank=True)
    icon_code_2 = models.CharField(max_length=60,null=True,blank=True)
    icon_code_3 = models.CharField(max_length=60,null=True,blank=True)
    icon_code_4 = models.CharField(max_length=60,null=True,blank=True)
    image= models.FileField(max_length=200 , upload_to="Why_Choose_Us_Section/", null=True,blank=True)
    mobile_background_image= models.FileField(max_length=200 , upload_to="Why_Choose_Us_Section/", null=True,blank=True)
    background_image= models.FileField(max_length=200 , upload_to="Why_Choose_Us_Section/", null=True,blank=True)

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Why Choose Us Section"  # Plural name (same as singular, to avoid pluralization)
