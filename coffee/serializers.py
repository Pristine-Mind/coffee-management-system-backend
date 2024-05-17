from rest_framework import serializers

from coffee.models import Coffee


class CoffeeSerializer(serializers.ModelSerializer):
    roast_type_display = serializers.CharField(
        source='get_roast_type_display',
        read_only=True
    )

    class Meta:
        model = Coffee
        fields = '__all__'
