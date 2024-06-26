# Generated by Django 4.2.13 on 2024-05-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Is price paid for table'),
        ),
        migrations.AddField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('vacant', 'Vacant'), ('occupied', 'Occupied')], default='vacant', max_length=255, verbose_name='Table Status'),
        ),
    ]
