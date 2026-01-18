from django.urls import path
from .views import (
    list_books, LibraryDetailView,
    register_view, login_view, logout_view,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    path('books/', list_books, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Role-Based URLs
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
