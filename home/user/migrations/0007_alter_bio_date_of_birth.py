# Generated by Django 4.2.7 on 2024-01-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='date_of_birth',
            field=models.DateField(help_text='yyyy/mm/dd'),
        ),
    ]
