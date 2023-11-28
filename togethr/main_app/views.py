from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

# account settings
@login_required
def edit_posts(request):
    return render(request, 'menu/account/edit_posts.html')

@login_required
def edit_profile(request):
    return render(request, 'menu/account/edit_profile.html')

@login_required
def delete_profile(request):
    return render(request, 'menu/account/delete_profile.html')


# nav menu
@login_required
def profile(request):
    return render(request, 'menu/profile.html')

@login_required
def account_settings(request):
    return render(request, 'menu/account_settings.html')

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, 'menu/profile_list.html', {"profiles": profiles}) 



