from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
        editable=False,
    )
    phone_number = models.CharField(
        verbose_name=_('phone number'),
        blank=True,
        null=True,
        max_length=100
    )
    last_frontend_login = models.DateTimeField(
        verbose_name=_('last frontend login'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
