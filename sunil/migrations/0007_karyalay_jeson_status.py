# Generated by Django 5.0.6 on 2024-09-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunil', '0006_karyalay_booking_show_status_karyalay_show_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyalay',
            name='jeson_status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
