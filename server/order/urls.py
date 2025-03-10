from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

# Using DefaultRouter() to automatically generate standard CRUD API endpoints
# for the OrderViewSet, which handles Create (C), Read (R), Update (U), and Delete (D) operations.
# This approach simplifies API routing and ensures consistency with RESTful standards.

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),  # Includes all generated routes for CRUD operations
]
