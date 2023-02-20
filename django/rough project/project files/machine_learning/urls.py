from django.urls import path
from . import views

urlpatterns = [
    path('dt/', views.dt,name='dt_path'),
    path('knn/', views.knn,name='ml_path'),
   
]
