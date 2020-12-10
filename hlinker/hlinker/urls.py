from django.contrib import admin
from django.urls import path, include

from .views import about_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('links/', include('links.urls')),
]
