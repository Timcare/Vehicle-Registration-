# Generated by Django 4.2.7 on 2024-02-11 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_profiles_approved_alter_bio_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2028, 2, 11, 4, 1, 50, 98801), editable=False),
        ),
    ]
