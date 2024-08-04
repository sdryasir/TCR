from django.contrib import admin

# Register your models here.
from .models import Blog


# Register your models here.
class Blog_Admin(admin.ModelAdmin):
    list_display = ['title','tag','image','Blog_details_heading_1','Blog_details_description_1','Blog_details_description_2','Blog_details_heading_2','Blog_details_heading_2_description','feature_1','feature_2','feature_3','blog_details_image','tips_heading','tips_description']

admin.site.register(Blog,Blog_Admin)