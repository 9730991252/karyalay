from django.urls import path
from ajax import views


urlpatterns = [
    path('indraprastha/<int:id>', views.indraprastha,name='indraprastha'),    
]