# Generated by Django 3.1 on 2020-09-13 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200913_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='reply_to',
            new_name='reply',
        ),
        migrations.RemoveField(
            model_name='auctionlistings',
            name='bid',
        ),
        migrations.AddField(
            model_name='bids',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.auctionlistings'),
            preserve_default=False,
        ),
    ]
