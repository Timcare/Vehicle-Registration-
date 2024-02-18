from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from home.constants import BLOOD_GROUP,CLASS_OF_VEHICLE
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Create your models here.

class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    approved=models.BooleanField(default=False,null=True)
    photo=models.ImageField(upload_to='user_profile',null=True,blank=True)
    objects=models.Manager()


    def __str__(self) -> str:
        return f'{self.user.username} profile'

class Bio(models.Model):
    profiles=models.OneToOneField(Profiles,on_delete=models.CASCADE,null=True)
    middlename=models.CharField(max_length=120,blank=True,null=True)
    date_of_birth=models.DateField(help_text='yyyy/mm/dd')
    state=models.CharField(max_length=120)
    local_government=models.CharField(max_length=120)
    blood_group=models.CharField(max_length=2,choices=BLOOD_GROUP)
    upload_driving_school_certificate=models.FileField(upload_to='driving_school_certificate')
    class_of_vehicle=models.CharField(max_length=120,choices=CLASS_OF_VEHICLE)
    issue_date=models.DateField(help_text='yyyy/mm/dd',default=timezone.now)
    expiry_date=models.DateField(default=datetime.now() + relativedelta(years=4),editable=False)









