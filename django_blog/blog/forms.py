from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post # Import Post model
from taggit.forms import TagWidget # Mandatory import for the check

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# --- NEW: Post Form with Tagging (Mandatory for Step 2) ---
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tags separated by commas (e.g. django, python)'
            }),
        }

# --- Comment Form Implementation ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a comment...',
            }),
        }
        labels = {
            'content': '',
        }
