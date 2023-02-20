from django.urls import path
from . import views

urlpatterns = [
    path('nn/', views.nn,name='nn_path'),
  
   
]
