from .models import About
from about_us.decorators import listen_unread
from au_auth.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

@login_required
@listen_unread
def index(request):
    feeds = reversed(About.objects.all())
    context = {
        'feeds':feeds,
    }

    return render(request, 'au_about/feed.jinja2', context)

@login_required
@listen_unread
def positive(request, item_id):
    about = About.objects.get(id=item_id)
    about.positive_votes += 1
    about.save()

    return redirect(reverse("au_about:index"))

@login_required
@listen_unread
def negative(request, item_id):
    about = About.objects.get(id=item_id)
    about.negative_votes += 1
    about.save()

    return redirect(reverse("au_about:index"))

@login_required
@listen_unread
def new(request):
    form = request.POST
    user_id = request.user.id
    if form:
        comment = form.get('comment')
        profile_id = form.get('profile')
        profile = Profile.objects.get(id=profile_id)
        new_about = About.objects.create(
            comment=comment,
            positive_votes=0,
            negative_votes=0,
            profile=profile,
        )
    return redirect(reverse("au_about:index"))

