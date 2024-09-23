# Generated by Django 5.0.7 on 2024-09-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='barangay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='landmark',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='municipality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='province',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
