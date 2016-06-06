from django.shortcuts import render
from .models import About

def index(request):
    feeds = About.objects.all()
    context = {
        'feeds':feeds
    }

    return render(request, 'au_about/feed.jinja2', context)

