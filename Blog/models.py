from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150,null=True)
    tag = models.CharField(max_length=20,null=True)
    image= models.FileField(max_length=200 , upload_to="Blog/", null=True)


    category = models.CharField(max_length=150,null=True)
    Blog_details_heading_1 = models.CharField(max_length=150,null=True,blank=True)
    Blog_details_description_1 = models.CharField(max_length=700,null=True,blank=True)
    Blog_details_description_2 = models.CharField(max_length=700,null=True,blank=True)
    
    Blog_details_heading_2 = models.CharField(max_length=150,null=True,blank=True)
    Blog_details_heading_2_description = models.CharField(max_length=700,null=True,blank=True)

    feature_1 = models.CharField(max_length=150,null=True,blank=True)
    feature_2 = models.CharField(max_length=150,null=True,blank=True)
    feature_3 = models.CharField(max_length=150,null=True,blank=True)
    blog_details_image= models.FileField(max_length=200 , upload_to="Blog/", null=True,blank=True)

    tips_heading = models.CharField(max_length=150,null=True,blank=True)
    tips_description = models.CharField(max_length=700,null=True,blank=True)




    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Blog"  # Plural name (same as singular, to avoid pluralization)