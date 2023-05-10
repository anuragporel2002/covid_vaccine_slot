from django.db import models
from django.utils import timezone
import datetime

class StateName(models.Model):
    name=models.TextField(max_length=25,null=False,primary_key=True)

    def __str__(self):
        return self.name

class City(models.Model):
    state=models.ForeignKey(StateName,on_delete=models.CASCADE,null=True)
    name=models.TextField(max_length=25,null=False,primary_key=True)

    def __str__(self):
        return self.name

class VaccineCentre(models.Model):
    name=models.TextField(max_length=75,null=False)
    working_hour_start=models.TimeField(null=False,default=timezone.now)
    working_hour_end=models.TimeField(null=False,default=timezone.now)
    address=models.TextField(max_length=250,null=False)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    state=models.ForeignKey(StateName,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class AppointmentDetails(models.Model):
    index=models.IntegerField(null=False)
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(null=False)
    centre=models.ForeignKey(VaccineCentre,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=False)
    date=models.DateField(null=False,default=datetime.date.today)

    def __str__(self):
        return self.name
