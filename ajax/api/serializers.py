from owner.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Event
        fields = ['id','event_name']