from django.shortcuts import render
from sunil.models import *
from django.http import JsonResponse
import json
# Create your views here.
def indraprastha(request, id):
    data = Karyalay.objects.values().filter(id=id).first()
    return JsonResponse(data)
    