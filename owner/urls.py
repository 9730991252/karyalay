from django.urls import path
from owner import views


urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard,name='owner_dashboard'),    
    path('event/', views.event,name='event'),    
    path('images/', views.images,name='images'),    
    path('map/', views.map,name='map'),    
    path('video/', views.video,name='video'),
    path('woner_logout/', views.woner_logout,name='woner_logout'),    
    path('profile/', views.profile,name='profile'),    
    
]