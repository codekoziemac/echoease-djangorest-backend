# Generated by Django 5.0.7 on 2024-10-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_payer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('downpayment', 'Down Payment'), ('final_payment', 'Final Payment'), ('payout', 'Payout'), ('refund', 'Refund')], max_length=50),
        ),
    ]
