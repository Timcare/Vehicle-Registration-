from django.db import models
from .constants import VEHICLE_CATEGORY,FUEL_TYPE,VEHICLE_TYPE,ENGINE_TYPE,OWNER_TYPE,TITLE
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    vehicle_category=models.CharField(max_length=12,choices=VEHICLE_CATEGORY)
    vehicle_sub_category=models.CharField(max_length=120,null=True,blank=True)
    old_plate_number=models.IntegerField(null=True,blank=True)
    vehicle_maker=models.CharField(max_length=120)
    color=models.CharField(max_length=120)
    fuel_type=models.CharField(max_length=10,choices=FUEL_TYPE)
    year_of_manufacturer=models.IntegerField()
    plate_number=models.CharField(max_length=10)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_category}'

class VehicleInfo(models.Model):
    model=models.CharField(max_length=120)
    engine_number=models.IntegerField(blank=True,null=True)
    policy_number=models.IntegerField(blank=True,null=True)
    vehicle_type=models.CharField(max_length=120,choices=VEHICLE_TYPE)
    chassis_no=models.IntegerField()
    engine_capacity=models.CharField(max_length=50,choices=ENGINE_TYPE)
    tank_capacity=models.IntegerField()
    odometer=models.IntegerField(blank=True,null=True)
    vehicle=models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.model}'

class OwnerInfo(models.Model):
    owner_identification=models.CharField(max_length=50,choices=OWNER_TYPE)

class Individual(models.Model):
    title=models.CharField(max_length=20,choices=TITLE)
    first_name=models.CharField(max_length=120)
    middle_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    identification_no=models.IntegerField()
    email_address=models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=120,blank=True,null=True)
    city=models.CharField(max_length=120)
    mobile_number=models.IntegerField()
    state=models.CharField(max_length=120)
    local_government=models.CharField(max_length=120)


class Company(models.Model):
    company_name=models.CharField(max_length=120)
    identification_no=models.IntegerField()
    email_address=models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=120,blank=True,null=True)
    city=models.CharField(max_length=120)
    mobile_number=models.IntegerField()
    state=models.CharField(max_length=120)
    local_government=models.CharField(max_length=120)


# class OtherInfo(models.Model):
#     drivers_license_number=models.IntegerField(blank=True,null=True)
#     license_bearer_number=models.IntegerField(blank=True,null=True)
#     state_of_plate_number_allocation=models.CharField(max_length=120,blank=True,null=True)
#     request_fancy_number_plate=models.BooleanField(blank=True)


