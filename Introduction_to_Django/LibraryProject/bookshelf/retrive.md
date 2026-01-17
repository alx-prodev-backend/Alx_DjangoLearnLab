# Retrieve Operation

```python
books = Book.objects.all()
books
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = Book.objects.get(title="1984")
book
# Output: <Book: 1984 by George Orwell (1949)>
