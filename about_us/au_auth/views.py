from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Profile

def index(request):
    make_login(request)
    return render(request, 'about_us/teste.html')


def make_login(request):
    if request.POST:
        form = request.POST
        user_name = form.get('user')
        password = form.get('pass')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = "Login Realizado com Sucesso"
            else:
                message = "Usuário não está ativo"
        else:
            message = "Senha ou Usuário incorreto"

        return redirect(reverse('au_about:index'))

def make_logout(request):
    logout(request)
    context = {
        'user':request.user
    }
    return render(request, "au_auth/login.jinja2")

def show_profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    print(profiles)
    return render(request, 'au_auth/profiles.jinja2', context)

def show_profile(request, profile_pk):
    profile = Profile.objects.get(id=profile_pk)
    abouts = profile.about_set.all()
    context = {
        'profile':profile,
        'abouts':abouts,
    }

    return render(request, 'au_auth/profile.jinja2', context)
