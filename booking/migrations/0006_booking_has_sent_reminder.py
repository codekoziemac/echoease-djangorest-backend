# Generated by Django 5.0.7 on 2024-10-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking_cancelled_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='has_sent_reminder',
            field=models.BooleanField(default=False),
        ),
    ]
