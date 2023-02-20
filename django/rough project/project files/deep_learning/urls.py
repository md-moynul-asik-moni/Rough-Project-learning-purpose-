from django.urls import path
from . import views

urlpatterns = [
    path('d/', views.deepLearning),
   
]
