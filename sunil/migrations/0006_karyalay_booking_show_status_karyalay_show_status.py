# Generated by Django 5.0.6 on 2024-08-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunil', '0005_alter_karyalay_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyalay',
            name='booking_show_status',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='karyalay',
            name='show_status',
            field=models.IntegerField(default=1, null=True),
        ),
    ]