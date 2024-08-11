from django.db import models

# Create your models here.
class About_Counter_Description(models.Model):
    description_1 = models.CharField(max_length=600,null=True)
    description_2 = models.CharField(max_length=600,null=True)






    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "About Description"  # Plural name (same as singular, to avoid pluralization)