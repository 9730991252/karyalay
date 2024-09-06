from django.shortcuts import render
from sunil.models import *
from owner.models import *
from django.http import JsonResponse
# Create your views here.
def search_lucky_day(request):
    if request.method == 'GET':
        k_id = request.GET['k_id']
        year = request.GET['year']
        month = request.GET['month']
        day = Lucky_day.objects.values().filter(karyalay_id=k_id,status=1,year=year,month=month)
        lucky_day = list(day)
        print(lucky_day)
    return JsonResponse({'lucky_day':lucky_day})
