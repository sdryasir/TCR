from django.db import models

# Create your models here.
class Counter_Section(models.Model):
    description = models.TextField(max_length=300,blank=True)  
    number_of_feature = models.CharField(max_length=60,null=True)
    sign_of_feature = models.CharField(max_length=2,null=True)
    feature = models.CharField(max_length=60,null=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Counter Section"  # Plural name (same as singular, to avoid pluralization)