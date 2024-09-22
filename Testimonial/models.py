from django.db import models

# Create your models here.

class Testimonial(models.Model):
    description = models.CharField(max_length=500,null=True)
    image= models.FileField(max_length=200 , upload_to="Testimonial/", null=True)
    name = models.CharField(max_length=60,null=True)
    post = models.CharField(max_length=60,null=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Testimonial"  # Plural name (same as singular, to avoid pluralization)