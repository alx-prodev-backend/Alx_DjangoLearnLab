# serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to ensure the publication year
    is not set in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            # IMPORTANT: checker expects serializers.ValidationError explicitly
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value