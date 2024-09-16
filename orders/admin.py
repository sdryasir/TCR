from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'status', 'stripe_session_id', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['id', 'stripe_session_id']

admin.site.register(Order, OrderAdmin)
