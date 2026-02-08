from django.db import models

# Create your models here.
# Creating Author table
class Author(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book table with FK relationship
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
