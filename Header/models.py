from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.validators import RegexValidator
# Create your models here.



def validate_image_format(image):

    if not image.name.endswith('.png'):
        raise ValidationError('Only PNG images are allowed.')

    # Additional check to validate image format (optional)
    try:
        image_format = image.file.content_type
        if image_format != 'image/png':
            raise ValidationError('Only PNG images are allowed.')
    except Exception as e:
        raise ValidationError('Invalid image format.')

class Header(models.Model):
    link1_name = models.CharField(max_length=15,blank=True)
    link1  = models.CharField(max_length=15,blank=True)
    link2_name = models.CharField(max_length=15,blank=True)
    link2 = models.CharField(max_length=60,blank=True)
    link3_name = models.CharField(max_length=15,blank=True)
    link3 = models.CharField(max_length=60,blank=True)
    dropdownlinks_name= models.CharField(max_length=15,blank=True)
    link4_name = models.CharField(max_length=15,blank=True)
    link4 = models.CharField(max_length=60,blank=True)
    link5_name = models.CharField(max_length=15,blank=True)
    link5 = models.CharField(max_length=60,blank=True)
    link6_name = models.CharField(max_length=15,blank=True)
    link6 = models.CharField(max_length=60,blank=True)
    link7_name = models.CharField(max_length=15,blank=True)
    link7 = models.CharField(max_length=60,blank=True)
    header_logo = models.ImageField(upload_to='images/', validators=[validate_image_format])
    side_navigation_image = models.ImageField(upload_to='images/', validators=[validate_image_format])
    side_navigation_description = models.CharField(max_length=300,blank=True)
    side_navigation_heading = models.CharField(max_length=15,blank=True)
    side_navigation_location = models.CharField(max_length=100,blank=True)
    side_navigation_email = models.CharField(max_length=100,blank=True)
    side_navigation_phone = models.CharField(
        max_length=15,null=True,blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '03999999999'. Up to 11 digits allowed."
            )
        ],
        help_text="Enter a valid phone number."
    )

    side_navigation_schedule = models.CharField(max_length=200,blank=True)
    side_navigation_facebook_link = models.CharField(max_length=300,blank=True)
    side_navigation_twitter_link = models.CharField(max_length=300,blank=True)
    side_navigation_instagram_link = models.CharField(max_length=300,blank=True)
    side_navigation_youtube_link = models.CharField(max_length=300,blank=True)
    side_navigation_rights = models.CharField(max_length=300,blank=True)



    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Header"  # Plural name (same as singular, to avoid pluralization)