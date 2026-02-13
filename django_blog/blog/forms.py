from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment # Import the new model

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

# --- NEW: Comment Form Implementation ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        # Adding Bootstrap classes for the professional UI look
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a comment...',
            }),
        }
        labels = {
            'content': '', # Keeps the UI clean by removing the "Content" label
        }