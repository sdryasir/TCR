from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_image_dimensions  # Adjust import as needed

# Create your models here.
class Main_Cars_Carousel(models.Model): 
    title_1 = models.CharField(max_length=60,blank=True)
    title_2 = models.CharField(max_length=60,blank=True)
    image = models.ImageField(
        max_length=200,
        upload_to="Main_Cars_Carousel/",
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_dimensions
        ]
    )

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Main Cars Carousel"  # Plural name (same as singular, to avoid pluralization)