from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Link


def link_view(request, link_url):
    try:
        link = Link.objects.get(short_link=link_url)
    except Exception as e:
        raise Http404('Link not found.')

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

    if data['description'] == None:
        pass
    
    user.link_set.create(
        name=data['name'],
        description=data['description'],
        parent_link=data['parent_link'],
        short_link='herby'
    )

    return HttpResponseRedirect('/links')
