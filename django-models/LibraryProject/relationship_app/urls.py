from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view for a specific library by ID
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
