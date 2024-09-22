from django.contrib import admin

# Register your models here.
from .models import Default_Background

class Default_Background_Admin(admin.ModelAdmin):
    list_display = ['About_Page_Title_1','About_Page_Title_2','About_Page_description_1','About_Page_description_2','Cars_Page_Title_1','Cars_Page_Title_2','Cars_Page_description_1','Cars_Page_description_2','Team_Page_Title_1','Team_Page_Title_2','Team_Page_description_1','Team_Page_description_2','Faq_Page_Title_1','Faq_Page_description_1','Blog_Page_Title_1','Blog_Page_Title_2','Blog_Page_description_1','Car_Details_Page_Title_1','Car_Details_Page_Title_2','Car_Details_Page_description_1','Car_Details_Page_description_2','Contact_Page_Title_1','Contact_Page_description_1','Login_Page_Title_1','Create_Account_Page_Title_1','Add_Your_Car_Page_Title','Bookings_Page_Title','image']

admin.site.register(Default_Background,Default_Background_Admin)