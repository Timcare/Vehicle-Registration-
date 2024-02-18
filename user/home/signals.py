from . models import Vehicle
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save,sender=Vehicle)
def create_plate_number(sender,instance,**kwargs):
    if not instance.plate_number:
        counter=1111
        counter+=1
        plateno=f"{counter}-NIG".lower()
    instance.plate_number=plateno
            
