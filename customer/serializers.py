from rest_framework import serializers


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
            user.profile.save()
        except Exception:
            raise serializers.ValidationError('Could not create user profile.')
