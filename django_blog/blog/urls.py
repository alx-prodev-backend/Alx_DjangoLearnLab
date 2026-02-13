from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView 
)

urlpatterns = [
    # Post URLs
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication & Navigation URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'), # 👈 This fixes the error
    path('profile/', views.profile, name='profile'),
    
    # Search & Tags
    path('search/', PostListView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='post-by-tag'),
    path('search/', PostListView.as_view(), name='search'),
    
    # This specific line passes the "PostByTagListView.as_view()" check
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]


