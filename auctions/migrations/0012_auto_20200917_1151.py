# Generated by Django 3.1 on 2020-09-17 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_bids_current_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bids',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
