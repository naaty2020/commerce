# Generated by Django 3.1 on 2020-09-14 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200913_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won', to=settings.AUTH_USER_MODEL),
        ),
    ]
