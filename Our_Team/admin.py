from django.contrib import admin

# Register your models here.

from .models import Our_Team

class Our_Team_Admin(admin.ModelAdmin):
    list_display = ['name','profession','facebook_link','twitter_link','instagram_link','image']

admin.site.register(Our_Team,Our_Team_Admin)