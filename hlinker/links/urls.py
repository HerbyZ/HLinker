from django.urls import path

from .views import link_list_view

app_name = 'links'
urlpatterns = [
    path('', link_list_view, name='link_list'),
]