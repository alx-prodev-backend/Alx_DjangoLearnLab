from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # on_delete=models.CASCADE means if a user is deleted, their posts are deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()  # Adds many-to-many relationship automatically

    def __str__(self):
        return self.title

    # Fixed: This must be indented INSIDE the Post class to work
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# --- NEW: Comment Model Implementation ---

class Comment(models.Model):
    # Links to the Post; related_name allows access via post.comments.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'