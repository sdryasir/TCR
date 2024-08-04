from django.db import models

# Create your models here.
class Choose_Car_Options(models.Model):
    car_option = models.CharField(max_length=60,null=True)
