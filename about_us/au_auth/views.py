from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def index(request):
    make_login(request)
    return render(request, 'about_us/teste.html')


def make_login(request):
    print("AAAAAAAAAAAAAAAAAAAAA")
    user = authenticate(username="aluno", password="aluno")
    if user is not None:
        if user.is_active:
            login(request, user)
    return render(request, 'about_us/teste.html')
