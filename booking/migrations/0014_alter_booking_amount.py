# Generated by Django 5.0.7 on 2024-11-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_alter_booking_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
