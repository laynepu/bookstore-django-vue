from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from category.models import Category
from .serializers import BookSerializer
import random

@api_view(['GET'])
def book_by_id(request, book_id):
    """
    GET /books/{book_id}
    Retrieve a single book by ID
    """
    book = get_object_or_404(Book, pk=book_id)
    return Response(BookSerializer(book).data)

@api_view(['GET'])
def books_by_category_id(request, category_id):
    """
    GET /books/by-category-id/{category_id}
    Retrieve books by category ID
    """
    category = get_object_or_404(Category, pk=category_id)
    books = Book.objects.filter(category=category)
    return Response(BookSerializer(books, many=True).data)

@api_view(['GET'])
def suggested_books(request, category_id):
    """
    GET /books/by-category-id/{category_id}/suggested?limit={limit}
    Retrieve a random selection of books by category ID
    """
    limit = int(request.GET.get('limit', 3))  # Default to 3
    books = list(Book.objects.filter(category_id=category_id))
    random_books = random.sample(books, min(len(books), limit))
    return Response(BookSerializer(random_books, many=True).data)

@api_view(['GET'])
def books_by_category_name(request, category_name):
    """
    GET /books/by-category-name/{category_name}
    Retrieve books by category name
    """
    category = get_object_or_404(Category, name=category_name)
    books = Book.objects.filter(category=category)
    return Response(BookSerializer(books, many=True).data)

@api_view(['GET'])
def suggested_books_by_category_name(request, category_name):
    """
    GET /books/by-category-name/{category_name}/suggested?limit={limit}
    Retrieve a random selection of books by category name
    """
    limit = int(request.GET.get('limit', 3))  # Default to 3
    category = get_object_or_404(Category, name=category_name)
    books = list(Book.objects.filter(category=category))
    random_books = random.sample(books, min(len(books), limit))
    return Response(BookSerializer(random_books, many=True).data)
