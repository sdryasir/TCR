from django.contrib import admin

# Register your models here.

from .models import Main_Hero_Section

class Main_Hero_Section_Admin(admin.ModelAdmin):
    list_display = ['title_1','title_2','description_1','description_2','video_link','price','image']

admin.site.register(Main_Hero_Section,Main_Hero_Section_Admin)