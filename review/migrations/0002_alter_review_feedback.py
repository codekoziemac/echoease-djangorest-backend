# Generated by Django 5.0.7 on 2024-10-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
