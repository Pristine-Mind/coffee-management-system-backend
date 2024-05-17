from typing import Union

from rest_framework import serializers

from order.models import Order, OrderItem, Table
from main.writable_nested_serializers import (
    NestedCreateMixin,
    NestedUpdateMixin,
)


class OrderSerializer(serializers.ModelSerializer):
    size_display = serializers.CharField(
        source='get_size_display',
        read_only=True
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(
    NestedUpdateMixin,
    NestedCreateMixin,
    serializers.ModelSerializer
):
    order = OrderSerializer(many=True)
    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    table_amount = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = '__all__'

    def get_table_amount(self, obj: Table) -> Union[int | None]:
        # return the latest amount of the table
        queryset = OrderItem.objects.filter(
            table=obj,
            table__status=Table.Status.OCCUPIED
        ).order_by(
            '-ordered_at'
        )
        print(queryset)
        if queryset.exists():
            return queryset.first().price
        return None

    def create(self, validated_data):
        raise serializers.ValidationError("Create is not allowed")

    def update(self, instance, validated_data):
        is_paid = validated_data.get('is_paid')
        if is_paid:
            validated_data['status'] = Table.Status.VACANT
            validated_data['price'] = None
        return super().update(instance, validated_data)
