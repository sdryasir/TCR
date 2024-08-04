from django.contrib import admin

from .models import Background_Video


# Register your models here.
class Background_Video_Admin(admin.ModelAdmin):
    list_display = ['title_line_1','title_line_2','description','download_button','video']

admin.site.register(Background_Video,Background_Video_Admin)