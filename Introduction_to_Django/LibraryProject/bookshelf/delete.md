# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
books
# Output: <QuerySet []>
