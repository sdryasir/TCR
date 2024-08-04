from django.contrib import admin

# Register your models here.

from .models import Counter_Section

class Counter_Section_Admin(admin.ModelAdmin):
    list_display = ['description','number_of_feature','sign_of_feature','feature']

admin.site.register(Counter_Section,Counter_Section_Admin)