from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import UserProfile

class User_Profile_Admin(admin.ModelAdmin):
    list_display = ['user','phone','address_line_1','address_line_2','postal_code','province','pickup_date','return_date']

admin.site.register(UserProfile,User_Profile_Admin)
=======
>>>>>>> a0ee3231e3195dbb9bcccc64a2e44a660ea7c0d6
