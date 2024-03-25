# Generated by Django 4.2.11 on 2024-03-25 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='small', max_length=100, verbose_name='Coffee Size')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('preparing', 'Preparing'), ('completed', 'Completed')], default='pending', max_length=100, verbose_name='Status')),
                ('has_milk', models.BooleanField(default=False)),
                ('has_sugar', models.BooleanField(default=False)),
                ('milk_amount', models.IntegerField(blank=True, null=True, verbose_name='Milk Amount')),
                ('sugar_amount', models.IntegerField(blank=True, null=True, verbose_name='Sugar Amount')),
                ('water_amount', models.IntegerField(blank=True, null=True, verbose_name='Water Amount')),
                ('quantity', models.IntegerField(blank=True, default=1, verbose_name='Quantity')),
                ('coffee_amount', models.IntegerField(blank=True, null=True, verbose_name='Coffee Amount')),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.coffee', verbose_name='Coffee')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
    ]