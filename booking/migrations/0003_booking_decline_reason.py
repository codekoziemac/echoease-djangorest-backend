# Generated by Django 5.0.7 on 2024-10-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_is_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='decline_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
