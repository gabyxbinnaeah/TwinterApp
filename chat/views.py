from django.shortcuts import render
from .models import Image,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login/')
def images(request):
    image_contents=Image.image_details()
    return render(request, 'all-chat/home.html',{"image_contents":image_contents})

def profile(request):
    profile_contents=Profile.profile_details()
    return render(request, 'all-chat/home.html',{"profile_contents":profile_contents})


def new_image(request):
    if request.method=='POST':
        form=ImageForm(request.POST)


