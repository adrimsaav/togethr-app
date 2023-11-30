from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': ''
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 1}),
        }