from django.urls import path 
from ajax.api import views


urlpatterns = [
    path('indraprastha/<int:k_id>/<int:m>/<int:y>', views.indraprastha,name='indraprastha'), 
]