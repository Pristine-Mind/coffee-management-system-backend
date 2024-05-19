from rest_framework import viewsets, permissions, pagination

from order.models import OrderItem, Table
from order.serializers import (
    OrderItemSerializer,
    TableSerializer
)
from order.filter_set import OrderItemFilterSet


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilterSet
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        return OrderItem.objects.all()


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Table.objects.all()
