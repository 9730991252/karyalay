# Generated by Django 5.0.6 on 2024-05-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunil', '0003_rename_add_karyalay_karyalay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karyalay',
            name='owner_name',
        ),
        migrations.AddField(
            model_name='karyalay',
            name='owner_name_english',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='karyalay',
            name='owner_name_marathi',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
