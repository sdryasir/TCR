from django.contrib import admin

# Register your models here.


from .models import Choose_Car_Options

class Choose_Car_Option_Admin(admin.ModelAdmin):
    list_display = ['car_option']

admin.site.register(Choose_Car_Options,Choose_Car_Option_Admin)