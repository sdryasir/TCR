from django.contrib import admin

# Register your models here.
from .models import Book_Your_Drive

class Book_Your_Drive_Admin(admin.ModelAdmin):
    list_display = ['title_line_1','title_line_2','des_line_1','des_line_2','book_now_button','background_image','mobile_background_image']

admin.site.register(Book_Your_Drive,Book_Your_Drive_Admin)