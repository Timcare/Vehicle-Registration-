from django.contrib import admin
from .models import Vehicle,VehicleInfo

# Register your models here.
class VehicleInfoAdmin(admin.ModelAdmin):
    list_display=('model','vehicle_type','chassis_no','engine_capacity','tank_capacity')
    list_filter=['tank_capacity']
    search_fields=['model']
    fieldsets = [
        ("Vehicle Information", {
            "fields": [
                'model','engine_number','policy_number','vehicle_type','chassis_no','engine_capacity','tank_capacity','odometer','approved','vehicle'
            ],
        }),
    ]
    

admin.site.register(Vehicle)
admin.site.register(VehicleInfo,VehicleInfoAdmin)

