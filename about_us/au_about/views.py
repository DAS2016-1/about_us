from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import About

def index(request):
    feeds = About.objects.all()
    context = {
        'feeds':feeds,
    }

    return render(request, 'au_about/feed.jinja2', context)

def positive(request, item_id):
    about = About.objects.get(id=item_id)
    about.positive_votes += 1
    about.save()

    return redirect(reverse("au_about:index"))

def negative(request, item_id):
    about = About.objects.get(id=item_id)
    about.negative_votes += 1
    about.save()

    return redirect(reverse("au_about:index"))
