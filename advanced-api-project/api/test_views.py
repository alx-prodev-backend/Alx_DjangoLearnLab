# test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        #Author Creation
        self.author = Author.objects.create(name="John Doe")

        # BOOK creation
        self.book1 = Book.objects.create(
            title="Python Basics",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Advanced Django",
            publication_year=2021,
            author=self.author
        )

        # URL endpoints
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])


    # --- List Books ---
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # --- Retrieve single Book ---
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # --- Create Book ---
    def test_create_book(self):
        data = {
            'title': "New Book",
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # --- Update Book ---
    def test_update_book(self):
        data = {'title': "Updated Title"}
        response = self.client.patch(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # --- Delete Book ---
    def test_delete_book(self):
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    # --- Filtering by title ---
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Python Basics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # --- Searching ---
    def test_search_books_by_author(self):
        response = self.client.get(self.list_url, {'search': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    # --- Ordering ---
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)


