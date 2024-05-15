from django.urls import path
from home import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),    
    path('karyalay_filter/', views.karyalay_filter,name='karyalay_filter'),    
    path('karyalay_detail/<int:id>/', views.karyalay_detail,name='karyalay_detail'),    
    path('booked_date', views.booked_date,name='booked_date'),    
    
]