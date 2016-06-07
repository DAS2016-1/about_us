from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import About
from au_auth.models import Profile

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

def new(request):
    form = request.POST
    user_id = request.user.id
    if form:
        comment = form.get('comment')
        print("Commend: ",comment)
        profile_id = form.get('profile')
        profile = Profile.objects.get(id=profile_id)
        new_about = About.objects.create(
            comment=comment,
            positive_votes=0,
            negative_votes=0,
            profile=profile,
        )
    return redirect(reverse("au_about:index"))

