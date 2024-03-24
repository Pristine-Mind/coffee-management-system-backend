from rest_framework import (
    views,
    viewsets,
    response,
    permissions,
    status,
    mixins,
    serializers,
)

from coffee.models import Coffee
from coffee.serializers import CoffeeSerializer


class CoffeeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CoffeeSerializer

    def get_queryset(self):
        return Coffee.objects.all()

