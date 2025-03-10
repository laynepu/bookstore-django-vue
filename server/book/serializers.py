from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """ Serializer for the Book model with camelCase keys """
    bookId = serializers.IntegerField(source="id")
    isPublic = serializers.BooleanField(source="is_public")
    isFeatured = serializers.BooleanField(source="is_featured")
    categoryId = serializers.IntegerField(source="category.id", allow_null=True)

    class Meta:
        model = Book
        fields = ["bookId", "title", "author", "description", "price", "rating", "isPublic", "isFeatured", "categoryId"]
