# Generated by Django 3.1 on 2020-09-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlistings_bids_category_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]