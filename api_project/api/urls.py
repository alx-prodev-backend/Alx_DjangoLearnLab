from os.path import basename

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList


# create router and register the viewset
router  =DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLS for BOokViewSet (full CRUD)
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name= 'api_token_auth' ), # Token endpoint

]