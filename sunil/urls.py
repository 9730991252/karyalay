from django.urls import path
from sunil import views


urlpatterns = [
    path('sunil_dashboard/', views.sunil_dashboard,name='sunil_dashboard'),    
    path('add_karyalay/', views.add_karyalay,name='add_karyalay'),    
    
]