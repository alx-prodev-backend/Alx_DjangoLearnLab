from django.urls import path
from .views import list_books, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='books_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
