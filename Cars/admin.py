from django.contrib import admin

# Register your models here.
from .models import CARS

class CARS_Admin(admin.ModelAdmin):
    list_display = ['name','image','new_car','category','passengers','stock','price','petrol_diesel','automatic_manual','at_mt','car_image_1','car_image_2','car_image_3','car_image_4','rating_per','reviews','description','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6']

admin.site.register(CARS,CARS_Admin)