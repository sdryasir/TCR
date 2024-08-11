from django.contrib import admin

# Register your models here.
from .models import About_Counter_Description

class About_Counter_Description_Admin(admin.ModelAdmin):
    list_display = ['description_1','description_2']

admin.site.register(About_Counter_Description,About_Counter_Description_Admin)