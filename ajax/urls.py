from django.urls import path
from ajax import views


urlpatterns = [
    path('search_lucky_day/', views.search_lucky_day,name='search_lucky_day'),    
]