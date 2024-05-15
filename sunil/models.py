from django.db import models

# Create your models here.

class Karyalay(models.Model):
    karyalay_name_marathi=models.CharField(max_length=500)
    karyalay_name_eglish=models.CharField(max_length=500)
    nearby_location_marathi=models.CharField(max_length=500)
    nearby_location_eglish=models.CharField(max_length=500)
    address_marathi=models.CharField(max_length=500)
    address_eglish=models.CharField(max_length=500)
    pin_code=models.IntegerField(null=True)
    owner_name_marathi=models.CharField(max_length=500,null=True)
    owner_name_english=models.CharField(max_length=500,null=True)
    mobile=models.IntegerField(unique=True)
    pin=models.IntegerField()
    status=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True,null=True)


