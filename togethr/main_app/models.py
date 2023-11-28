from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save 


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

# Create Profile when User is created
# kwargs will accept all our unnecessary data
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # make user follow themself
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)