from django.db import models

# Create your models here.
class Default_Background(models.Model):
    About_Page_Title_1 = models.CharField(max_length=60,blank=True)
    About_Page_Title_2 = models.CharField(max_length=60,blank=True)
    About_Page_description_1 = models.TextField(max_length=100,blank=True)
    About_Page_description_2 = models.TextField(max_length=100,blank=True)  
    
    
    Cars_Page_Title_1 = models.CharField(max_length=60, null=True,blank=True)
    Cars_Page_Title_2 = models.CharField(max_length=60,blank=True)
    Cars_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)
    Cars_Page_description_2 = models.TextField(max_length=100,blank=True)  
    
    Team_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)
    Team_Page_Title_2 = models.CharField(max_length=60,blank=True)
    Team_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)
    Team_Page_description_2 = models.TextField(max_length=100,blank=True)  
    
    Faq_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)
    Faq_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)
    
    Blog_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)
    Blog_Page_Title_2 = models.CharField(max_length=60,blank=True)
    Blog_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)

    Car_Details_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)
    Car_Details_Page_Title_2 = models.CharField(max_length=60,blank=True)
    Car_Details_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)
    Car_Details_Page_description_2 = models.TextField(max_length=100,blank=True)  

    Contact_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)
    Contact_Page_description_1 = models.TextField(max_length=100,null=True,blank=True)

    Login_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)

    Create_Account_Page_Title_1 = models.CharField(max_length=60,null=True,blank=True)

    

    image= models.FileField(max_length=200 , upload_to="Default_Background/", null=True)
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Default Background"  # Plural name (same as singular, to avoid pluralization)   