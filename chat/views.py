from django.shortcuts import render,redirect, get_object_or_404
from .models import Image,Profile,Comment,Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,ProfileFormm,CommentForm,UpdateImageFormm,UpdateProfileForm,UpdateUserForm,UpdateCommentsForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf
from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image_contents=Image.image_details()
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'all-chat/home.html',{"image_contents":image_contents[::1],"users":users})
    
@login_required(login_url='/accounts/login/')
def profile(request):
    # currentUserId=request.user.id  currentUserId
    profile_contents=Profile.profile_details()
    return render(request, 'all-chat/home.html',{"profile_contents":profile_contents})


@login_required(login_url='/accounts/login/')
def profile(request, username):
    images = request.user.profile.images.all()
    print(images)
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        profileForm = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileForm.is_valid():
            userform.save()
            profileForm.save()
            return HttpResponseRedirect(request.path_info)
    else:
        userform = UpdateUserForm(instance=request.user)
        profileForm = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'userform': userform,
        'profileForm': profileForm,
        'images': images,
    }
    return render(request, 'profile.html', params)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profileUrl')
    else:
        form = UploadForm()
    return render(request,'update_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def follow(request, to_follow):
    if request.method == 'GET':
        next_user_profile = Profile.objects.get(pk=to_follow)
        following_list = Follow(follower=request.user.profile, following=next_user_profile)
        following_list.save()
        return redirect('user_profile', next_user_profile.user.username)









def new_image(request):
    
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            posted_image=form.save(commit=False)
            posted_image.user=request.user.profile
            posted_image.save()

            return redirect('homeUrl')

    else:
        form=ImageForm()

    return render(request, 'all-chat/new_image.html',{"form":form}) 

          
            





