from django.contrib import admin
from .models import General_Questions
# Register your models here.



# Register your models here.
class General_Questions_Admin(admin.ModelAdmin):
    list_display = ['Question','Answer']

admin.site.register(General_Questions,General_Questions_Admin)