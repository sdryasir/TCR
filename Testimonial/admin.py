from django.contrib import admin
from .models import Testimonial
# Register your models here.


class Testimonial_Admin(admin.ModelAdmin):
    list_display = ['description','image','name','post']

admin.site.register(Testimonial,Testimonial_Admin)