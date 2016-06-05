from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Profile

def index(request):
    make_login(request)
    return render(request, 'about_us/teste.html')


def make_login(request):
    print("AAAAAAAAAAAAAAAAAAAAA")
    user = authenticate(username="aluno", password="aluno")
    if user is not None:
        if user.is_active:
            login(request, user)
            message = "Login Realizado com Sucesso"
        else:
            message = "Usuário não está ativo"
    else:
        message = "Senha ou Usuário incorreto"

    user = request.user
    profile = Profile.objects.get(id=user.id)
    context = {'message':message, 'user':profile}
    return render(request, 'au_auth/profile.jinja2',context)
