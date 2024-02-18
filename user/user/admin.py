from django.contrib import admin
from .models import Bio,Profiles

# Register your models here.
class BioAdmin(admin.ModelAdmin):
    list_display=('date_of_birth','state','local_government','blood_group','class_of_vehicle','issue_date','expiry_date')

admin.site.register(Profiles)
admin.site.register(Bio,BioAdmin)
