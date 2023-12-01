from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment, User, Photo
from django.views.generic import DeleteView
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout, login
import uuid
import boto3
import os 

@login_required
def timeline(request):
    form = PostForm()
    comment_form = CommentForm()
    posts = Post.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if 'post_form' in request.POST:
            form = PostForm(request.POST)
            photo_file = request.FILES.get('photo-file', None)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                if photo_file:
                    s3 = boto3.client('s3')
                    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                    try:
                        bucket = os.environ['S3_BUCKET']
                        s3.upload_fileobj(photo_file, bucket, key)
                        url = f"{os.environ['S3_BASE_URL']}/{bucket}/{key}"
                        Photo.objects.create(url=url, post=post)
                    except Exception as e:
                        print('An error occurred uploading file to S3')
                        print(e)
                return redirect('timeline')
        elif 'comment_form' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.post_id = request.POST.get('post_id')
                comment.save()
                return redirect('timeline')
    return render(request, 'timeline.html', {
        'form': form,
        'comment_form': comment_form,
        'posts': posts,
        'comments': comments
    })


def home(request):
    if request.user.is_authenticated:
        return redirect('timeline')
    else:
        return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('timeline')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'menu/profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

    # Code follow/unfollow button
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
                current_user_profile.save()

        return render(request, 'menu/profile.html', {"profile":profile})
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def account_settings(request):
    return render(request, 'menu/account_settings.html')


def like_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.like.filter(id=request.user.id):
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        return redirect('timeline')
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def like_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=pk)
        if comment.like.filter(id=request.user.id):
            comment.like.remove(request.user)
        else:
            comment.like.add(request.user)
        return redirect('timeline')
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def logout(request):
    return redirect('home')


# account settings
@login_required
def edit_posts(request):
    return render(request, 'menu/account/edit_posts.html')

@login_required
def edit_profile(request):
    return render(request, 'menu/account/edit_profile.html')

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name ='menu/account/delete_profile.html'
    success_url = '/'




# nav menu

@login_required
def account_settings(request):
    return render(request, 'menu/account_settings.html')

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'menu/profile_list.html', {"profiles": profiles}) 

