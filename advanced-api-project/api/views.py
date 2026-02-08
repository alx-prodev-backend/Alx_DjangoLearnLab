from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import   Book
from .serializers import  BookSerializer

# Create your views here.
# starter way
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Book
from .serializers import BookSerializer


class ListView(ListAPIView):
    """
    Retrieve all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(RetrieveAPIView):
    """
    Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateView(CreateAPIView):
    """
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(UpdateAPIView):
    """
    Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(DestroyAPIView):
    """
    Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ِAdvanced way
class BookViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on  Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

