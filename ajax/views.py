from django.shortcuts import render
from sunil.models import *
from django.http import JsonResponse
import json
# Create your views here.
def indraprastha(request, id):
    data_raw = Karyalay.objects.values().filter(id=id)
    data=list(data_raw)
    return JsonResponse({'data':data,})
    