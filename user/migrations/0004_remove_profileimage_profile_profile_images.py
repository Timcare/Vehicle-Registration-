# Generated by Django 4.2.7 on 2023-12-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profileimage'),
        ),
    ]
