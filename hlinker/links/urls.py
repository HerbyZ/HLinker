from django.urls import path

from .views import (
    link_list_view, create_link_view,
    create_link_page_view, link_view,
    delete_link_view, login_page_view,
    login_view, register_page_view,
    logout_view, register_view
)

app_name = 'links'
urlpatterns = [
    path('', link_list_view, name='link_list'),
    path('link/<str:link_url>', link_view, name='link'),
    path('new/', create_link_page_view, name='new_link'),
    path('create/', create_link_view, name='create_link'),
    path('delete/<str:link_url>', delete_link_view, name='delete_link'),
    path('login/', login_page_view, name='login_page'),
    path('login/l/', login_view, name='login'),
    path('register/', register_page_view, name='register_page'),
    path('register/r', register_view, name='register'),
    path('logout/', logout_view, name='logout')
]