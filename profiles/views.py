from django.shortcuts import render

# Create your views here.
# profiles/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

def profile_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})
