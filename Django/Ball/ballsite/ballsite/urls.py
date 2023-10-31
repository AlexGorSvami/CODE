from django.contrib import admin
from django.urls import path, include
from player import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player/', include('player.urls')),
]
