# Generated by Django 4.2.7 on 2024-02-10 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_vehicleinfo_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleinfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicleinfo',
            name='vehicle',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.vehicle'),
        ),
    ]