from django.db import models
from sunil.models import *
from PIL import Image 

# Create your models here.
class Event(models.Model):
    karyalay = models.ForeignKey(Karyalay,on_delete=models.PROTECT,null=True)
    event_name=models.CharField(max_length=500)
    parti_name=models.CharField(max_length=500,null=True)
    event_date=models.DateField()
    status=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True,null=True)


class Images(models.Model):
    karyalay = models.ForeignKey(Karyalay,on_delete=models.PROTECT,null=True)
    image_1= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_2= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_3= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_4= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_5= models.ImageField(upload_to="images",default="",null=True,blank=True)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        image_1 = Image.open(self.image_1.path)
        output_size = (300,300)
        image_1.thumbnail(output_size)
        image_1.save(self.image_1.path)



        image_2 = Image.open(self.image_2.path)
        output_size = (300,300)
        image_2.thumbnail(output_size)
        image_2.save(self.image_2.path)

        image_3 = Image.open(self.image_3.path)
        output_size = (300,300)
        image_3.thumbnail(output_size)
        image_3.save(self.image_3.path)

        image_4 = Image.open(self.image_4.path)
        output_size = (300,300)
        image_4.thumbnail(output_size)
        image_4.save(self.image_4.path)


        image_5 = Image.open(self.image_5.path)
        output_size = (300,300)
        image_5.thumbnail(output_size)
        image_5.save(self.image_5.path)

class Map(models.Model):
    karyalay = models.ForeignKey(Karyalay,on_delete=models.PROTECT,null=True)
    map_code=models.CharField(max_length=500)


class Lucky_day(models.Model):
    karyalay = models.ForeignKey(Karyalay,on_delete=models.PROTECT,null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    lucky_day = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    status = models.IntegerField()