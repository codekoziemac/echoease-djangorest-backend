# Generated by Django 5.0.7 on 2024-11-14 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_payment_title'),
        ('transaction', '0005_transaction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
    ]
