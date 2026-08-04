from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date', 'status')
    search_fields = ('customer__name', 'status')
    list_filter = ('status', 'order_date')
    readonly_fields = ('order_id',)
    filter_horizontal = ('order_details',)