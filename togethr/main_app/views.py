from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

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

@login_required
def home(request):
    print("Current user:", request.user)  
    print("Is authenticated:", request.user.is_authenticated)  

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user  
            new_post.save()
            return redirect('home')
        else:
            print("Form errors:", form.errors)  
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    print(posts)
    return render(request, 'home.html', {'form': form, 'posts': posts})

