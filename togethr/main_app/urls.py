from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  # nav menu
  path('menu/profile/<int:pk>/', views.profile, name='profile'),
  path('menu/profile_list/', views.profile_list, name='profile_list'),
  path('menu/account_settings/', views.account_settings, name='account_settings'),
  # account settings page
  path('menu/account/edit_posts', views.edit_posts, name='edit_posts'),
  path('menu/account/edit_profile', views.edit_profile, name='edit_profile'),
  path('menu/account/delete_profile', views.delete_profile, name='delete_profile'),
  # create post from timeline
  path('timeline/', views.timeline, name='timeline'),
]
