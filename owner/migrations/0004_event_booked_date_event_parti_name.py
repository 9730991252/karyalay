# Generated by Django 5.0.6 on 2024-05-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_alter_event_karyalay'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booked_date',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='parti_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
