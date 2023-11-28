from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def profile_list(request):
    return render(request, 'profile_list.html') 

def home_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'form': form, 'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user  
            new_post.save()
            return redirect('home')  
    else:
        form = PostForm() 
    return render(request, 'post_create.html', {'form': form}) 
