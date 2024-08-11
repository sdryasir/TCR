from django.db import models

# Create your models here.
class Main_Cars_Carousel(models.Model):
    image= models.FileField(max_length=200 , upload_to="Main_Cars_Carousel/", null=True)

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Main Cars Carousel"  # Plural name (same as singular, to avoid pluralization)