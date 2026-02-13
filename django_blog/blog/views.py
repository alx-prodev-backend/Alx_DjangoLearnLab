from django.shortcuts import render
# blog/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
# Existing home/posts views...

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required  # Decorator
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'blog/profile.html', context)

# 1. List View (Accessible to all)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Use your existing home template
    context_object_name = 'posts'
    ordering = ['-date_posted']

# 2. Detail View (Accessible to all)
class PostDetailView(DetailView):
    model = Post

# 3. Create View (Login required)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Automatically set author
        return super().form_valid(form)

# 4. Update View (Author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Security Check

# 5. Delete View (Author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # Redirect home after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author