from django.urls import path
from . import consumers 
websocket_urlpatterns = [
     path('ws/',consumers.Video_camera.as_asgi()),
]