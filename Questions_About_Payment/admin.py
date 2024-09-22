from django.contrib import admin
from .models import Payment_Questions
# Register your models here.
class Payment_Questions_Admin(admin.ModelAdmin):
    list_display = ['Question','Answer']

admin.site.register(Payment_Questions,Payment_Questions_Admin)