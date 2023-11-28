from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile_list/', views.profile_list, name='profile_list'),
  path('post_create/', views.post_create, name='post_create'),
  path('', views.home_view, name='home'),
]