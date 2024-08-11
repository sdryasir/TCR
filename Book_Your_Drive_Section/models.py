from django.db import models

# Create your models here.
class Book_Your_Drive(models.Model):
    title_line_1 = models.CharField(max_length=100,null=True,blank=True)
    title_line_2 = models.CharField(max_length=100,null=True,blank=True)
    des_line_1 = models.CharField(max_length=100,null=True,blank=True)
    des_line_2 = models.CharField(max_length=100,null=True,blank=True)
    book_now_button = models.CharField(max_length=60,null=True,blank=True)
    background_image= models.FileField(max_length=200 , upload_to="Book_Your_Drive_Section/", null=True,blank=True)
    mobile_background_image= models.FileField(max_length=200 , upload_to="Book_Your_Drive_Section/", null=True,blank=True)


    
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Book Your Drive"  # Plural name (same as singular, to avoid pluralization)

