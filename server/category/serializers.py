from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source="id") # creates a new field in the serialized output

    class Meta:
        model = Category
        fields = ["categoryId", "name"]  # # Explicitly list fields, excluding `id`