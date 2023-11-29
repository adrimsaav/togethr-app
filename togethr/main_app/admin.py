from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from .models import Post

# Register your models here.

# Profile and User Info
class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # display username on admin page
    fields = ["username"]
    inlines = [ProfileInLine]

admin.site.register(Post)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

