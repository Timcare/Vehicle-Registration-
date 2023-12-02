from django.db import models
from .constants import VEHICLE_CATEGORY,FUEL_TYPE,VEHICLE_TYPE,ENGINE_TYPE

# Create your models here.
class Vehicle(models.Model):
    vehicle_category=models.CharField(max_length=12,choices=VEHICLE_CATEGORY)
    vehicle_sub_category=models.CharField(max_length=120)
    old_plate_number=models.IntegerField()
    vehicle_maker=models.CharField(max_length=120)
    color=models.CharField(max_length=120)
    fuel_type=models.CharField(max_length=10,choices=FUEL_TYPE)
    year_of_manufacturer=models.IntegerField()

class VehicleInfo(models.Model):
    model=models.CharField(max_length=120)
    engine_number=models.IntegerField()
    policy_number=models.IntegerField()
    vehicle_type=models.CharField(max_length=120,choices=VEHICLE_TYPE)
    chassis_no=models.IntegerField()
    engine_capacity=models.CharField(max_length=50,choices=ENGINE_TYPE)
    tank_capacity=models.IntegerField()
    odometer=models.IntegerField()

    def __str__(self):
        return f'{self.models}'


