from django.contrib import admin
from django.urls import path, include
from player import views
from player.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('player.urls')),
]

handler404 = page_not_found
