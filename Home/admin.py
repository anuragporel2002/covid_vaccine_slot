from django.contrib import admin
from .models import StateName,City, VaccineCentre,AppointmentDetails

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=['name','state']
    search_fields=['name']
    list_filter=['state']

@admin.register(VaccineCentre)
class CentreAdmin(admin.ModelAdmin):
    list_display=['name','working_hour_start','working_hour_end','address','city','state']
    search_fields=['name']
    list_filter=['city','state']

@admin.register(AppointmentDetails)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['index','name','mobile','email','centre','date']
    search_fields=['name']
    list_filter=['date','centre']

admin.site.register(StateName)
