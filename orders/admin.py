from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'total_amount', 'status','payment_status','payment_id']

admin.site.register(Order,OrderAdmin)