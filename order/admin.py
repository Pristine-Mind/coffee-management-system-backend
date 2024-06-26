from django.contrib import admin

from order.models import Order, OrderItem, Table


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass
