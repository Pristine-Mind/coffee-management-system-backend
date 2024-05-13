from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from coffee.models import Coffee


class Table(models.Model):
    name = models.CharField(
        verbose_name=_('Name of table')
    )


class Order(models.Model):
    class CoffeeSize(models.TextChoices):
        SMALL = 'small', _('Small')
        MEDIUM = 'medium', _('Medium')
        LARGE = 'large', _('Large')

    coffee = models.ForeignKey(
        Coffee,
        on_delete=models.CASCADE,
        verbose_name=_('Coffee')
    )
    size = models.CharField(
        max_length=100,
        choices=CoffeeSize.choices,
        default=CoffeeSize.SMALL,
        verbose_name=_('Coffee Size')
    )
    has_milk = models.BooleanField(default=False)
    has_sugar = models.BooleanField(default=False)
    milk_amount = models.IntegerField(
        verbose_name=_('Milk Amount'),
        null=True, blank=True)
    sugar_amount = models.IntegerField(
        verbose_name=_('Sugar Amount'),
        null=True, blank=True
    )
    water_amount = models.IntegerField(
        verbose_name=_('Water Amount'),
        null=True, blank=True
    )
    quantity = models.IntegerField(
        verbose_name=_('Quantity'),
        default=1, blank=True
    )
    coffee_amount = models.IntegerField(
        verbose_name=_('Coffee Amount'),
        null=True, blank=True
    )

    def __str__(self):
        return f"Order: {self.id} - {self.coffee.name}"


class OrderItem(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PREPARING = 'preparing', _('Preparing')
        COMPLETED = 'completed', _('Completed')

    ordered_at = models.DateTimeField(auto_now_add=True)
    order = models.ManyToManyField(Order, blank=True, verbose_name=_("Order"))
    customer = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('Customer'),
    )
    table = models.ForeignKey(
        Table,
        verbose_name=_('Order of table'),
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name=_('Status')
    )
    price = models.IntegerField(
        verbose_name=_('Price'),
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.table} - {self.price}'


@receiver(m2m_changed, sender=OrderItem.order.through)
def create_comms_group(sender, instance, action, **kwargs):
    if action == 'post_add':
        total_price = sum(order.coffee.price * order.quantity for order in instance.order.all())
        instance.price = total_price
        instance.save()
