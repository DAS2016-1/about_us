from django.shortcuts import render
from .models import About

def index(request):
    feed = About.objects.all()[0]
    context = {
        'feed':feed
    }

    return render(request, 'au_about/feed.jinja2', context)

