# Generated by Django 4.2.7 on 2023-12-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_vehicle_fuel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year_of_manufacturer',
            field=models.IntegerField(),
        ),
    ]
