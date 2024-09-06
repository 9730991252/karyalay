from django.urls import path 
from ajax.api import views


urlpatterns = [
    path('indraprastha_api/', views.indraprastha_api,name='indraprastha_api'), 
]