from ajax.api.serializers import *

from owner .models import Event
from django.http import HttpResponse

from django.http import JsonResponse

def indraprastha(request,k_id,m,y):
    if request.method == 'GET':
        m=int(m)
        if m < 10:
            m=f'0{m}'
        d=f"{y}-{m}-"
        b=Event.objects.values().filter(event_date__icontains=d,karyalay_id=k_id)
        if b:
            book=list(b)
    return JsonResponse({'book':book})
         