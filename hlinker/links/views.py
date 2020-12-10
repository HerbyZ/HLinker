from django.http.response import Http404
from django.shortcuts import render

from .models import Link, User


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
