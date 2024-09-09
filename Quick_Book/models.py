from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Quick_Book(models.Model):
    name = models.CharField(max_length=60,blank=True)
    car = models.CharField(max_length=60,null=True,blank=True)
    phone = models.CharField(
        max_length=15,null=True,blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '03999999999'. Up to 11 digits allowed."
            )
        ],
        help_text="Enter a valid phone number."
    )
    email = models.CharField(max_length=60, null=True,blank=True)
    
    
    
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Quick Booking"  # Plural name (same as singular, to avoid pluralization)
