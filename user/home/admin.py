from django.contrib import admin
from .models import Vehicle,VehicleInfo,Vehicle,OwnerInfo,Individual,Company,VehicleProof

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

class VehicleAdmin(admin.ModelAdmin):
    list_display=('vehicle_category','vehicle_maker','color','fuel_type','year_of_manufacturer','plate_number','user')


admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleInfo,VehicleInfoAdmin)
admin.site.register(VehicleProof)

