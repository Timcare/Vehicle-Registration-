# Generated by Django 4.2.7 on 2024-01-20 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_vehicle_vehicle_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='title',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Mr.', 'Mr.'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.'), ('Engr.', 'Engr.'), ('Chief.', 'Chief.'), ('Rev.', 'Rev.'), ('Alhaji.', 'Alhaji.'), ('Alhaja.', 'Alhaja.'), ('Immam.', 'Immam.'), ('Pastor.', 'Pastor.'), ('Engineer.', 'Engineer.')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ownerinfo',
            name='owner_identification',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Company RC Number', 'Company RC Number'), ("Driver's License", "Driver's License"), ('International Passport', 'International Passport'), ('National ID Card', 'National ID Card'), ('Tax Clearance Number', 'Tax Clearance Number'), ('Tax Identification Number', 'Tax Identification Number')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Petrol', 'Petrol'), ('Disel', 'Disel'), ('Bio-Fuel', 'Bio-Fuel'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_category',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Private', 'Private')], max_length=12),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='engine_capacity',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Above 3.0', 'Above 3.0'), ('Below 1.6', 'Below 1.6'), ('Between 1.6 and 2.0', 'Between 1.6 and 2.0'), ('Between 2.1 and 3.0', 'Between 2.1 and 3.0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='vehicle_type',
            field=models.CharField(choices=[(None, '---SELECT---'), ('Bus', 'Bus'), ('Crane', 'Crane'), ('Motor cycle', 'Motor cycle'), ('Pick up', 'Pick up'), ('Salon', 'Salon'), ('SUV', 'SUV'), ('Tractor', 'Tractor'), ('Truck', 'Truck'), ('Van', 'Van'), ('Wagon', 'Wagon')], max_length=120),
        ),
    ]
