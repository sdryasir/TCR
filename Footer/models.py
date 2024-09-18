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

class Footer(models.Model):
    description = models.CharField(max_length=300,blank=True)
    logo = models.ImageField(upload_to='images/', validators=[validate_image_format])
    links_heading= models.CharField(max_length=20,blank=True)
    link1_name = models.CharField(max_length=15,blank=True)
    link1  = models.CharField(max_length=15,blank=True)
    link2_name = models.CharField(max_length=15,blank=True)
    link2 = models.CharField(max_length=60,blank=True)
    link3_name = models.CharField(max_length=15,blank=True)
    link3 = models.CharField(max_length=60,blank=True)
    link4_name = models.CharField(max_length=15,blank=True)
    link4 = models.CharField(max_length=60,blank=True)
    contact_heading= models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=100,blank=True)
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
    news_letter_heading= models.CharField(max_length=20,blank=True)
    facebook_link= models.CharField(max_length=400,blank=True)
    twitter_link= models.CharField(max_length=400,blank=True)
    youtube_link= models.CharField(max_length=400,blank=True)
    whatsapp_link= models.CharField(max_length=400,blank=True)
    rights= models.CharField(max_length=200,blank=True)
    terms_and_conditions_link= models.CharField(max_length=400,blank=True)
    privacy_policy_link= models.CharField(max_length=400,blank=True)





    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Footer"  # Plural name (same as singular, to avoid pluralization)
