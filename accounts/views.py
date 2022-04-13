from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_view(request):
    social = request.user.social_auth.get(provider='discord')

    return render(request, "accounts/profile_view.html", {
        'title': "Profile",
        'user_details': social.extra_data
    })
