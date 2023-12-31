from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

  
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.logout, name='logout'),
  # nav menu
  path('profile/<int:pk>/', views.profile, name='profile'),
  path('profile_list/', views.profile_list, name='profile_list'),
  path('account_settings/', views.account_settings, name='account_settings'),
  # account settings page
  path('account/edit_profile', views.edit_profile, name='edit_profile'),
  path('profile/<int:pk>/delete_profile/', views.ProfileDelete.as_view(), name='delete_profile'),
  # create post from timeline
  path('timeline/', views.timeline, name='timeline'),
  # track likes for post
  path('like_post/<int:pk>/', views.like_post, name='like_post'),
  # track likes for comment
  path('like_comment/<int:pk>/', views.like_comment, name='like_comment'),
  # delete posts
  path('post/<int:pk>/delete_post/', views.delete_post, name='delete_post'),
  # delete comments
  path('comment/<int:pk>/delete_comment/', views.delete_comment, name='delete_comment'),
  # change password
  path('account/change_password/', views.change_password, name='change_password'),

]
