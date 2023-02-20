from django.urls import path
from . import views

urlpatterns = [
    path('bt/', views.bt,name='bt_path'),
    path('btd/', views.btd, name='btd_path'),
    path('df/', views.df,name= 'df_path'),
    path('register/', views.register,name= 'df_register'),
    path('cv/', views.cv.as_view()),
   
]
