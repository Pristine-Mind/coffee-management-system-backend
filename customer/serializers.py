from rest_framework import serializers

from django.contrib.auth.models import User

from order.serializers import OrderItemSerializer


class RegistrationSerializer(serializers.Serializer):
    # required fields
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)

    # optional fields
    phone_number = serializers.CharField(
        required=False,
        max_length=255,
        write_only=True
    )
    address = serializers.CharField(
        max_length=255,
        write_only=True,
        required=False
    )

    def validate_username(self, username):
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError('A user with that username already exists.')
        return email

    def save(self):
        # using email as username for user registration
        username = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']

        phone_number = self.validated_data.get('phone_number')
        address = self.validated_data.get('address')

        # Create the User object
        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_active=True
            )
        except Exception:
            raise serializers.ValidationError('Could not create user.')

        try:
            user.profile.phone_number = phone_number
            user.profile.address = address
            user.profile.save()
        except Exception:
            raise serializers.ValidationError('Could not create user profile.')


class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source="profile.address", read_only=True)
    orders = OrderItemSerializer(read_only=True, source="orderitem_set", many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "address",
            "orders"
        )


class SuperUserSerializer(serializers.ModelSerializer):
    total_sales = serializers.SerializerMethodField()
    total_items = serializers.SerializerMethodField()
    total_remaining_items = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "total_sales",
            "total_items",
            "total_remaining_items"
        )

    def get_total_sales(self, obj):
        pass

    def get_total_items(self, obj):
        pass

    def get_total_remaining_items(self, obj):
        pass
