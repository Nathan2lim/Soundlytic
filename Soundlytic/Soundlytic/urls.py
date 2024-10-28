from django.contrib import admin
from django.urls import path, include
from SoundlytiApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500




urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('SoundlytiApp.urls')),
    #path('',include('SoundlyticStat.urls')),
    #path('',include('SoundlyApple.urls')),
    #path('',include('SoundlySpo.urls')),

    ]

    