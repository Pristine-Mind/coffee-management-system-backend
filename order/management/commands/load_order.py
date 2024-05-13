from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from order.models import Order, OrderItem, Table
from coffee.models import Coffee


class Command(BaseCommand):
    help = 'Load data into Order and OrderItem tables'

    def handle(self, *args, **kwargs):
        coffee_list = [coffee for coffee in Coffee.objects.all()]
        table_list = [table for table in Table.objects.all()]
        quantities = [1, 2, 3, 4, 5]
        statuses = [status for status in OrderItem.OrderStatus]
        sizes = [size for size in Order.CoffeeSize]

        for i in range(50):
            coffee = coffee_list[i % len(coffee_list)]
            quantity = quantities[i % len(quantities)]
            table = table_list[i % len(table_list)]
            status = statuses[i % len(statuses)]
            size = sizes[i % len(sizes)]

            # Create order
            order = Order.objects.create(
                coffee=coffee,
                size=size,
                has_milk=True,
                has_sugar=False,
                milk_amount=50,
                quantity=quantity,
                coffee_amount=100
            )

            # Create order item
            order_item = OrderItem.objects.create(
                ordered_at=datetime.now(),
                customer=User.objects.first(),
                status=status,
                table=table,
                price=1
            )
            order_item.order.add(order)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
