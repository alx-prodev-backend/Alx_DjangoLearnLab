from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality by title and author
    search_fields = ('title', 'author')

    # Add filters by publication_year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)