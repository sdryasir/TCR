from django.db import models

# Create your models here.
class Our_Team(models.Model):
    name = models.CharField(max_length=60)
    profession = models.CharField(max_length=60)
    facebook_link = models.TextField(max_length=300,null=True,blank=True)  
    twitter_link = models.TextField(max_length=300,null=True,blank=True)  
    instagram_link = models.TextField(max_length=300,null=True,blank=True)  
    image= models.FileField(max_length=200 , upload_to="Our_Team/", null=True)

    
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Team Cards"  # Plural name (same as singular, to avoid pluralization)