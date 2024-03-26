from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate

from rest_framework import (
    viewsets,
    views,
    response,
    status
)
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer


def bad_request(message):
    return JsonResponse({"statusCode": 400, "error_message": message}, status=400)


class RegistrationView(views.APIView):

    def post(self, request, version=None):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data, status=status.HTTP_200_OK
        )


class LoginView(views.APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)


        user = authenticate(username=username, password=password)
        if user is not None:
            api_key, created = Token.objects.get_or_create(user=user)

            # Reset the key's created_at time each time we get new credentials
            if not created:
                api_key.created = timezone.now()
                api_key.save()

            # (Re)set the user's last frontend login datetime
            user.profile.last_frontend_login = timezone.now()
            user.profile.save()

            return JsonResponse(
                {
                    "token": api_key.key,
                    "username": username,
                    "first": user.first_name,
                    "last": user.last_name,
                    "expires": api_key.created + timedelta(7),
                    "id": user.id,
                }
            )
        else:
            return bad_request("Invalid username or password")
