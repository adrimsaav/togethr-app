from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/login/', views.login, name='login'),
  path('accounts/signup/', views.signup, name='signup'),
]