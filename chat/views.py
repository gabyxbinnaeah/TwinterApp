from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,ProfileFormm,UpdateImageFormm,UpdateProfileForm,UpdateUserForm,UpdateCommentsForm
# Create your views here.
# @login_required(login_url='/accounts/login/')
def images(request):
    image_contents=Image.image_details()
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'all-chat/home.html',{"image_contents":image_contents,"users":users})

def profile(request):
    profile_contents=Profile.profile_details()
    return render(request, 'all-chat/home.html',{"profile_contents":profile_contents})


def new_image(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            posted_image=form.save(commit=False)
            posted_image.user=request.user.profile
            posted_image.save()
            return('images')

        else:
            form=ImageForm()

        return render(request, 'all-chat/posted_image.html',{"form":form})

          
            





