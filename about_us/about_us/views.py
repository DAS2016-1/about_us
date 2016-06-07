from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

def index(request):
    if  isinstance(request.user, AnonymousUser):
        return redirect(reverse('au_auth:make_login'))
    else:
        return redirect(reverse('au_about:index'))

