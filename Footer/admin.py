from django.contrib import admin

# Register your models here.
from .models import Footer


class Footer_Admin(admin.ModelAdmin):
    list_display=['description','logo','links_heading','link1_name','link1', 'link2_name','link2','link3_name','link3','link4_name','link4','contact_heading','email','phone','news_letter_heading','facebook_link','twitter_link','youtube_link','whatsapp_link','rights','terms_and_conditions_link','privacy_policy_link']

admin.site.register(Footer, Footer_Admin)