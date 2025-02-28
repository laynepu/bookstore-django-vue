from django.urls import path
from .views import (
    book_by_id, books_by_category_id, suggested_books,
    books_by_category_name, suggested_books_by_category_name
)

urlpatterns = [
    path('<int:book_id>/', book_by_id),
    path('by-category-id/<int:category_id>/', books_by_category_id),
    path('by-category-id/<int:category_id>/suggested/', suggested_books),
    path('by-category-name/<str:category_name>/', books_by_category_name),
    path('by-category-name/<str:category_name>/suggested/', suggested_books_by_category_name),
]