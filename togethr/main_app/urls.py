from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.logout, name='logout'),
  # nav menu
  path('profile/<int:pk>/', views.profile, name='profile'),
  path('profile_list/', views.profile_list, name='profile_list'),
  path('account_settings/', views.account_settings, name='account_settings'),
  # account settings page
  path('account/edit_posts', views.edit_posts, name='edit_posts'),
  path('account/edit_profile', views.edit_profile, name='edit_profile'),
  path('profile/<int:pk>/delete_profile/', views.ProfileDelete.as_view(), name='delete_profile'),
  # create post from timeline
  path('timeline/', views.timeline, name='timeline'),
  # track likes for post
  path('like_post/<int:pk>/', views.like_post, name='like_post'),
  # track likes for comment
  path('like_comment/<int:pk>/', views.like_comment, name='like_comment'),
  # asw adding pictures
  path('profile/<int:pk>/add_photo/', views.add_photo, name='add_photo'),
  # delete post
  path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
  # delete comment
  path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
]
