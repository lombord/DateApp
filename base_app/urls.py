from django.urls import path

from .views import *

urlpatterns = [
    path('', profilesPage, name='home'),
    path('profile/<str:pk>', profilePage, name='profile'),
    path('register', registerPage, name='register'),
]
