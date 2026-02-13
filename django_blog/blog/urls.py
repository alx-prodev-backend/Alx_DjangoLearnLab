from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # Post URLs
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # --- Mandatory Comment URLs (Matching Step 5 requirements) ---
    
    # URL for creating a comment: /post/<pk>/comments/new/
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    
    # URL for updating a comment: /comment/<pk>/update/
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    
    # URL for deleting a comment: /comment/<pk>/delete/
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
