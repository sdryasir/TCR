from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Background_Video(models.Model):
    title_line_1 = models.CharField(max_length=60,null=True)
    title_line_2 = models.CharField(max_length=60,null=True)
    description = models.CharField(max_length=60,null=True)
    download_button = models.CharField(max_length=20,null=True)
    download_link = models.CharField(max_length=300,null=True,blank=True)   
    video = models.FileField(upload_to='videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])




    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Background Video"  # Plural name (same as singular, to avoid pluralization)