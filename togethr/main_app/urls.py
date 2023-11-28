from django.urls import path
from . import views

	
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('menu/profile/', views.profile, name='profile'),
  path('menu/profile_list/', views.profile_list, name='profile_list'),
  path('menu/account_settings/', views.account_settings, name='account_settings'),
]