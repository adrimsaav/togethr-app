from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import PasswordChangeForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Create A Post...', 'class': 'post-textarea'})
        }
        exclude = ["user", "like",]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 1, 'placeholder': 'Comment...', 'class': 'rounded'}),
        }
        exclude = ["user", "like",]

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

