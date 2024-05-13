from django.shortcuts import render

from rest_framework import viewsets

from order.models import OrderItem, Table
from order.serializers import OrderItemSerializer, TableSerializer
from order.filter_set import OrderItemFilterSet


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilterSet

    def get_queryset(self):
        return OrderItem.objects.all()


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.all()
