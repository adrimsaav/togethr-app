from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save 


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    
    # allows us to see the last time a profile was updated
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"

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