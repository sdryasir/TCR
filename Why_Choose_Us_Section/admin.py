from django.contrib import admin

# Register your models here.
from .models import Why_Choose_Us_Section

class Why_Choose_Us_Section_Admin(admin.ModelAdmin):
    list_display = ['heading','description','feature_1','feature_2','feature_3','feature_4','icon_code_1','icon_code_2','icon_code_3','icon_code_4','image','background_image','mobile_background_image']

admin.site.register(Why_Choose_Us_Section,Why_Choose_Us_Section_Admin)