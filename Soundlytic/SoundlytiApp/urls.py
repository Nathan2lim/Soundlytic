from django.contrib import admin
from django.urls import path
from SoundlytiApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500



urlpatterns = [
    path('', views.home, name='home'),
]