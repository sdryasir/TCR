from django.contrib import admin

# Register your models here.
from .models import Add_Your_Car_Section

class Add_Your_Car_Section_Admin(admin.ModelAdmin):
    list_display = ['title_line_1','title_line_2','des_line_1','des_line_2','add_car_button','background_image','mobile_background_image']

admin.site.register(Add_Your_Car_Section,Add_Your_Car_Section_Admin)