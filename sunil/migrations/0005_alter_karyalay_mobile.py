# Generated by Django 5.0.6 on 2024-05-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunil', '0004_remove_karyalay_owner_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyalay',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
    ]
