from django.contrib import admin

# Register your models here.
from .models import UserProfile

class User_Profile_Admin(admin.ModelAdmin):
    list_display = ['user','phone','address_line_1','address_line_2','postal_code','province','pickup_date','return_date']

admin.site.register(UserProfile,User_Profile_Admin)

