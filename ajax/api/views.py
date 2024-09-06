from ajax.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from owner .models import Event
from django.http import HttpResponse

from django.http import JsonResponse
#@api_view(['GET'])
def indraprastha_api(request):
    #ev = Event.objects.filter(karyalay_id=1)
    ev = Event.objects.values().filter(karyalay_id=1)
    lst=list(ev)
    return JsonResponse(lst,safe=False)
    #serializer= EventSerializer(ev,many=True)
    #json_data= JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
         