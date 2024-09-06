from ajax.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from owner .models import Event
from django.http import HttpResponse


@api_view(['GET'])
def indraprastha_api(request):
    ev = Event.objects.filter(karyalay_id=1)
    serializer= EventSerializer(ev,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
         