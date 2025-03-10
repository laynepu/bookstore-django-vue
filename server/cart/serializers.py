from rest_framework import serializers
from .models import ShoppingCart, ShoppingCartItem
from book.serializers import BookSerializer

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()  # Manually define `book` to embed `BookSerializer`,
                             # otherwise, it would default to displaying only `book_id`.

    class Meta:
        model = ShoppingCartItem # Specify the corresponding Model
        fields = ['book', 'quantity'] # Define the fields to include in serialization

class ShoppingCartSerializer(serializers.ModelSerializer):
    cartId = serializers.IntegerField(source="id")
    items = ShoppingCartItemSerializer(many=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ['cartId', 'surcharge', 'items', 'subtotal']

    def get_subtotal(self, obj):
        return obj.computed_subtotal()