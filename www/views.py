from django.contrib.auth import logout
from django.shortcuts import redirect, render


def index_view(request):
    """Index page"""
    return render(request, 'www/index.html', {
        'title': 'Home',
    }, content_type='text/html')


def logout_view(request):
    logout(request)
    return redirect('www.index')
