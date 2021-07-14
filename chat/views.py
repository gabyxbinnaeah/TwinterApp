from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .forms import UploadForm,ProfileForm,CommentForm,UpdateImageFormm,UpdateProfileForm,UpdateUserForm,UpdateUserProfileForm
from .models import Image,Profile,Comment,Follow

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    '''
    method that displays image properties
    '''
    images = Image.images()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'index.html', {"images":images[::1],"users":users})

def post(request):
    '''
    method that displays post 
    '''
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request,'post_image.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile_user(request,username):
    '''
    method that displays owner profile information
    '''
    images = request.user.profile.images.all()
    print(images) 
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,
    }
    return render(request, 'profile.html', params)

@login_required(login_url='/accounts/login/')
def update_user_profile(request):
    '''
    method that permits users to update their profile.
    '''
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile')
    else:
        form = UploadForm()
    return render(request,'edit_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search_user_profile(request):
    '''
    method that displays the searched user profile.
    '''
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You did not make a selection"
    return render(request, 'results.html', {'message': message})

@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.images.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    return render(request, 'user_profile.html', params)

@login_required(login_url='/accounts/login/')
def follow_user(request, to_follow):
    '''
    method that enable follow
    '''
    if request.method == 'GET':
        loyal_user = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=loyal_user)
        follow_s.save()
        return redirect('user_profile', loyal_user.user.username)

@login_required(login_url='/accounts/login/')
def unfollow_user(request, to_unfollow):
    '''
    method that enable unfollow 
    '''
    if request.method == 'GET':
        common_user_profile = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=common_user_profile)
        unfollow_d.delete()
        return redirect('user_profile', common_user_profile.user.username)



@login_required(login_url='/accounts/login/')
def comment(request, id):
    '''
    method that enable user to commet while their session is active.
    '''
    image = get_object_or_404(Image, pk=id)
    comments = image.comment.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = image
            comment.user = request.user.profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    params = {
        'image': image,
        'form': form,
        'comments':comments,
    }
    return render(request, 'post.html', params)