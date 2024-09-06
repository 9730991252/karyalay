from ajax.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from owner .models import Event


@api_view(['GET'])
def indraprastha_api(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'msg':"hi sunil"
        })
         