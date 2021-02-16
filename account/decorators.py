from django.http import HttpResponse    # FOR IMPORT html pages without desiegns
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def warpper_func(request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('account:home')
        else:
            return view_func(request, *args, **kwargs)

    return warpper_func
