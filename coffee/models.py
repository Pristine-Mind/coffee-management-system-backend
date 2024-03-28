from django.db import models
from django.utils.translation import gettext_lazy as _


class Coffee(models.Model):
    class CoffeeRoastType(models.TextChoices):
        DARK = 'dark', _('Dark')
        MEDIUM = 'medium', _('Medium')
        LIGHT = 'light', _('Light')

    name = models.CharField(
        max_length=255,
        verbose_name=_('Coffee Name')
    )
    price = models.IntegerField(
        verbose_name=_('Price of coffee'),
    )
    image = models.FileField(
        verbose_name=_('Image of coffee'),
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=_('Description of coffee'),
        null=True,
        blank=True
    )
    caffeine_content = models.DecimalField(
        verbose_name=_('Caffeine Content'),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    origin = models.CharField(
        verbose_name=_('Origin place of coffee'),
        null=True, blank=True
    )
    roast_type = models.CharField(
        verbose_name=_('Roast type'),
        null=True, blank=True,
        max_length=100,
        choices=CoffeeRoastType.choices,
    )
    flavor_notes = models.TextField(
        verbose_name=_('Flavor Notes'),
        null=True, blank=True
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
