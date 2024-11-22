# Generated by Django 5.0.7 on 2024-10-14 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('admin', 'Admin'), ('message', 'Message'), ('new_booking', 'New Booking'), ('new_follower', 'New Follower'), ('booking_confirmation', 'Booking Confirmation'), ('booking_rejected', 'Booking Rejected'), ('payment_reminder', 'Payment Reminder'), ('event_reminder', 'Event Reminder')], max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications_as_follower', to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.message')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
