from django.contrib import admin

# Register your models here.
from .models import Default_Background

class Default_Background_Admin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Default_Background,Default_Background_Admin)