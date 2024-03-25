from django.shortcuts import render

from rest_framework import viewsets

from order.models import OrderItem
from order.serializers import OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.all()
