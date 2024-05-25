from django.db import models
from embed_video.fields import EmbedVideoField
from owner.models import *

# Create your models here.
class You_Tube(models.Model):
    karyalay = models.ForeignKey(Karyalay,on_delete=models.PROTECT,null=True)
    url_1 = EmbedVideoField()  # same like models.URLField()
    url_2 = EmbedVideoField()  # same like models.URLField()