
from django.urls import path
from main import views


app_name = "main"

urlpatterns = [
  path('', views.MainPage.as_view(), name='index'),
  path('about/', views.AboutPage.as_view(), name='about'),
  
 
]
