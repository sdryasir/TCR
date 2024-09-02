from django.db import models

# Create your models here.
class Default_Background(models.Model):
    image= models.FileField(max_length=200 , upload_to="Default_Background/", null=True)

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Default Background"  # Plural name (same as singular, to avoid pluralization)   