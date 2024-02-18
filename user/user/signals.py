from .models import Profiles,Bio
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profiles.objects.create(user=instance)

# @receiver(pre_save, sender=Bio)
# def create_bio_profile(sender,instance,**kwargs):
#     if not instance.profiles:
#         instance.profiles=instance.profiles