from .models import Profile
from about_us.decorators import listen_unread
from au_about.models import About
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.shortcuts import render, redirect
from active_sessions.active_sessions import *

@login_required
def index(request):
    make_login(request)
    return redirect(reverse('au_about:index'))

def make_login(request):
    message = ""
    if request.POST:
        form = request.POST
        user_name = form.get('user').strip()
        password = form.get('pass').strip()
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = "Login Realizado com Sucesso"
                return redirect(reverse('au_about:index'))
            else:
                message = "Usuário não está ativo"
        else:
            message = "Senha ou Usuário incorreto"
    context = {'message':message}
    return render(request, "au_auth/login.jinja2", context)

def make_logout(request):
    logout(request)
    context = {
        'user':request.user
    }
    return render(request, "au_auth/login.jinja2")


@login_required
@listen_unread
def show_profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    return render(request, 'au_auth/profiles.jinja2', context)

@login_required
@listen_unread
def show_profile(request, profile_pk):
    profile = Profile.objects.get(id=profile_pk)
    if profile.user.id == request.user.id:
        profile.read_abouts()
        request.session['unread_abouts'] = 0
    abouts = reversed(profile.about_set.all())
    context = {
        'profile':profile,
        'abouts':abouts,
    }

    return render(request, 'au_auth/profile.jinja2', context)

def singup(request):
    form = request.POST
    if form:
        username = form.get('user')
        password = form.get('pass')
        email = form.get('email')
        user =  User.objects.create_user(username, email, password)
        user.save()

        profile = Profile.objects.create(user=user, int_number=3)
        return_page = "au_auth/login.jinja2"
    else:
        return_page = 'au_auth/signup.jinja2'

    return render(request, return_page)

def get_notification(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        unread_abouts = profile.unread_abouts
        context = {"unread_abouts":unread_abouts}
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )

@receiver(post_save, sender=About)
def my_handler(sender, **kwargs):
    profile = kwargs['instance'].profile
    profile.unread_abouts += 1
    profile.save()
