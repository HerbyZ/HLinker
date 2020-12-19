from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render

import string
import random

from .models import Link, User


def link_view(request, link_url):
    try:
        link = Link.objects.get(short_link=link_url)
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {
            'error_code': 404,
            'error_message': 'Link not found.'
        })

    link.follow_count += 1
    link.save()
    return HttpResponseRedirect(link.parent_link)


def link_list_view(request):
    try:
        user = request.user
    except:
        return render(request, 'error.html', {
            'error_code': 404,
            'error_message': 'You can not use this page before auth.'
        })
    
    user_links = Link.objects.filter(user=user)
    
    return render(request, 'links/list.html', {
        'links': user_links
    })


def create_link_page_view(request):
    return render(request, 'links/new.html')


def create_link_view(request):
    if not request.user.is_authenticated:
        raise Http404('You need to login to use this page.')

    user = request.user
    data = request.POST

    def generate_url():
        def create_url():
            url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            return url

        url = create_url()

        def check():
            try:
                link = Link.objects.get(short_link=url)
            except ObjectDoesNotExist:
                return 1

        c = check()
        while True:
            url = create_url()
            if check() == 1:
                return url

    try:
        if data['description'] == None:
                user.link_set.create(
                name=data['name'],
                parent_link=data['parent_link'],
                short_link='herby'
            )
        else:
            user.link_set.create(
                name=data['name'],
                description=data['description'],
                parent_link=data['parent_link'],
                short_link=generate_url()
            )
    except Exception as e:
        return render(request, 'error.html', {
            'error_code': 404,
            # 'error_message': 'All field are required!'
            'error_message': repr(e)
        })

    return HttpResponseRedirect('/links')


def delete_link_view(request, link_url):
    try:
        link = Link.objects.get(short_link=link_url)
        link.delete()
    except ObjectDoesNotExist:
        return render(request, 'error.html', {
            'error_code': 404,
            'error_message': 'Link not found.'
        })

    return HttpResponseRedirect('/links')


def login_page_view(request):
    if request.user.is_authenticated:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'You already authenticated.'
        })

    return render(request, 'links/login.html')


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'You already authenticated.'
        })

    data = request.POST

    try:
        username = data['username']
        password = data['password']
        account = authenticate(username=username, password=password)
        login(request, account)
        return HttpResponseRedirect('/')
    except Exception as e:
        return render(request, 'error.html', {
            'error_code': 404,
            'error_message': 'Wrong login or password'
        })


def register_view(request):
    if request.user.is_authenticated:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'You already authenticated.'
        })

    data = request.POST

    try:
        email = data['email']
        username = data['username']
        password = data['password']
        User.objects.create_user(email, username, password)
    except:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'Something went wrong or some required field is empty (all fields are required).'
        })

    return HttpResponseRedirect('/')


def register_page_view(request):
    if request.user.is_authenticated:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'You already authenticated.'
        })
    
    return render(request, 'links/register.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return render(request, 'error', {
            'error_code': 404,
            'error_message': 'You aren\'t authenticated.'
        })

    logout(request)
    return HttpResponseRedirect('/')
