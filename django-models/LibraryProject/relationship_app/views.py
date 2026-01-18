from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Library

# List of books (accessible by anyone)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ===== Secured Views =====

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        from .models import Author
        author = get_object_or_404(Author, pk=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('books_list')
    return render(request, 'relationship_app/add_book.html')


@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('books_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
