# Generated by Django 5.0.6 on 2024-05-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_event_booked_date_event_parti_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='booked_date',
        ),
    ]
