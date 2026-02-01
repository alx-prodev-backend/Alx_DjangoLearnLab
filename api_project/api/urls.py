from django.urls import path
from .views import BookList
from ..api_project.urls import urlpatterns

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]