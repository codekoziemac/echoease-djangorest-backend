# Generated by Django 5.0.7 on 2024-11-13 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='client',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='net_amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payer_email',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payer_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_gateway',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_intent_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='platform_fee',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='service_fee',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='status',
        ),
    ]
