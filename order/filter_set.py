import django_filters as filters

from order.models import OrderItem


class OrderItemFilterSet(filters.FilterSet):
    table = filters.NumberFilter(field_name='table')
    created_at__lte = filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte",
        input_formats=["%Y-%m-%d"]
    )
    created_at__gte = filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte",
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = OrderItem
        fields = ()
