from rest_framework import serializers

from order.models import Order, OrderItem
from main.writable_nested_serializers import NestedCreateMixin, NestedUpdateMixin

class OrderSerializer(serializers.ModelSerializer):
    size_display = serializers.CharField(source='get_size_display', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(
    NestedUpdateMixin,
    NestedCreateMixin,
    serializers.ModelSerializer
):
    order = OrderSerializer(many=True, required=False)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
