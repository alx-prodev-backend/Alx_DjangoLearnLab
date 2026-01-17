# query_samples.py
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relationship_app.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Queries
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")


def books_in_library(library_name):
    """List all books in a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")


def librarian_of_library(library_name):
    """Retrieve the librarian for a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian at {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library: {library_name}")

# Example Usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
