from django.contrib import admin

# Register your models here.
from .models import Header







class Header_Admin(admin.ModelAdmin):
    list_display=['link1_name','link1','link2_name','link2','link3_name', 'link3','dropdownlinks_name','link4_name','link4','link5_name','link5','link6_name','link6','link7_name','link7','header_logo','side_navigation_image','side_navigation_description','side_navigation_heading','side_navigation_location','side_navigation_email','side_navigation_phone','side_navigation_schedule','side_navigation_facebook_link','side_navigation_twitter_link','side_navigation_instagram_link','side_navigation_youtube_link','side_navigation_rights']

admin.site.register(Header, Header_Admin)