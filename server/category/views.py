from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def get_categories(request):
    """
    GET /categories
    Retrieve all categories
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_category_by_id(request, category_id):
    """
    GET /categories/{category_id}
    Retrieve a single category by ID
    """
    category = get_object_or_404(Category, pk=category_id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)