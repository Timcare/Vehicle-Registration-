# Generated by Django 4.2.7 on 2023-12-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_company_address_alter_company_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherinfo',
            name='request_fancy_number_plate',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
