from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    mobile_number=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.firstname} profile'





