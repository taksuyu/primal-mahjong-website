from django.contrib.auth import logout
from django.shortcuts import redirect, render


def index_view(request):
    """Index page"""
    return render(request, 'www/Svelte.html', {
        'title': 'Home',
        'template': 'App.svelte',
        'svelte_props': {
            'name': 'World' if not request.user.is_authenticated else request.user.username,
        },
    }, content_type='text/html')


def user_view(request, username):
    """Look at a user's profile; assuming that they allow it to be public."""
    # TODO: Check if a user's profile exists and is public
    # TODO: Pass only the public information about a user to the view
    pass


def logout_view(request):
    logout(request)
    return redirect('www.index')
