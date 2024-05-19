"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.urls import re_path as url

from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from coffee import views as coffee_views
from order import views as order_views
from customer.views import (
    RegistrationView,
    LoginView,
    MeView
)

router = routers.DefaultRouter()

router.register(r'coffee', coffee_views.CoffeeViewSet, basename='coffee')
router.register(r'order', order_views.OrderViewSet, basename='order')
router.register(r'table', order_views.TableViewSet, basename='table')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^api/v1/", include(router.urls)),
    url(r"^register", RegistrationView.as_view()),
    url(r"^login", LoginView.as_view()),
    # url(r"^me", MeView.as_view()),
    # Docs
    path("docs/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("api-docs/", SpectacularAPIView.as_view(), name='schema'),
    path("api-docs/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
