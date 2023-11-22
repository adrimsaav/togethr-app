from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    # user_id FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwagrs={'cat_id': self.id})
    