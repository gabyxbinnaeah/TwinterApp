from django.shortcuts import render
from .models import Image,Profile

# Create your views here.
def profile(request):
    profile_contents=Profile.profile_details()
    return render(request, 'all-chat/home.html',{"profile_contents":profile_contents})