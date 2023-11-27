from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # profile that user can also delete
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # be able to follow different profiles, related_name is to see who is following who
    # 'symmetrical' is for when whoever User follows, other User does not have to follow them.
    # 'blank' is for when you have 0 following
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

