from django.contrib import admin

# Register your models here.
from .models import Quick_Book
class Quick_Book_Admin(admin.ModelAdmin):
    list_display=['name','car','phone', 'email']

admin.site.register(Quick_Book, Quick_Book_Admin)