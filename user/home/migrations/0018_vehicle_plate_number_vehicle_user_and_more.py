# Generated by Django 4.2.7 on 2024-02-11 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_remove_vehicleinfo_user_remove_vehicleinfo_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicleinfo',
            name='vehicle',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='home.vehicle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='old_plate_number',
            field=models.IntegerField(null=True),
        ),
    ]