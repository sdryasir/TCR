from django.contrib import admin
from .models import Main_Cars_Carousel
# Register your models here.


class Main_Cars_Carousel_Admin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Main_Cars_Carousel,Main_Cars_Carousel_Admin)