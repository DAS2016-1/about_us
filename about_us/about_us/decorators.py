from functools import wraps
from au_auth.models import Profile

def listen_unread(view_func):
    def _decorator(request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        unread_abouts = profile.unread_abouts
        request.session['unread_abouts'] = unread_abouts
        response = view_func(request, *args, **kwargs)
        return response
    return wraps(view_func)(_decorator)
