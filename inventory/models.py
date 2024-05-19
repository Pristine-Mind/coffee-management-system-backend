from django.db import models
from django.utils.translation import gettext_lazy as _


class Inventory(models.Model):
    class InventoryType(models.TextChoices):
        COFFEE = 'coffee', _('Coffee')
        SUGAR = 'sugar', _('Sugar')

    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        verbose_name=_('Type of inventory'),
        max_length=255,
        choices=InventoryType.choices
    )
    amount = models.FloatField(
        verbose_name=_('Amount')
    )

    def __str__(self):
        return f'{self.get_type_display()} - {self.amount}'
