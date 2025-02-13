# Generated by Django 5.0.7 on 2024-11-20 06:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0013_artist_account_number'),
        ('booking', '0016_booking_latitude_booking_longitude'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('artist', 'client', 'event_date', 'start_time', 'end_time')},
        ),
    ]
