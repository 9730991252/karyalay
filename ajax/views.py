from django.shortcuts import render
from sunil.models import *
from django.http import JsonResponse
import json
# Create your views here.
def indraprastha(request):
    data_raw = Karyalay.objects.values().all()
    data=list(data_raw)
    return JsonResponse(data , safe=False)
    