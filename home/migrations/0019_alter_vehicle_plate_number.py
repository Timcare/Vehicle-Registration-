# Generated by Django 4.2.7 on 2024-02-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_vehicle_plate_number_vehicle_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]