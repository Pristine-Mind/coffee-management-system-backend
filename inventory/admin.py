from django.contrib import admin
from inventory.models import Inventory
from rangefilter.filters import DateTimeRangeFilterBuilder


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_filter = [
        (
            'created_at',
            DateTimeRangeFilterBuilder()
        ),
        'type'
    ]
