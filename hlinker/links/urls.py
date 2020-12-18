from django.urls import path

from .views import link_list_view, create_link_view, create_link_page_view, link_view

app_name = 'links'
urlpatterns = [
    path('', link_list_view, name='link_list'),
    path('link/<str:link_url>', link_view, name='link'),
    path('new/', create_link_page_view, name='new_link'),
    path('create/', create_link_view, name='create_link'),
]