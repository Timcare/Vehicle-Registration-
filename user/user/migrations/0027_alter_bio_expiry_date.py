# Generated by Django 4.2.7 on 2024-02-11 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_bio_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2028, 2, 11, 16, 13, 51, 946341), editable=False),
        ),
    ]
