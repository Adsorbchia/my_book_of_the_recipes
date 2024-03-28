from django.contrib import admin
from django.urls import  path
from users import views

app_name = "users"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('user-settings/', views.user_settings, name='user_settings'),
    #  path('profile/', views.show_profile, name='profile_user'),
    path('logout/', views.logout, name='logout'),
    ]
