from rest_framework.response import Response
from rest_framework import status, viewsets
from book.models import Book
from customer.models import Customer
from .models import Order, LineItem
from .serializers import OrderBasicSerializer, OrderDetailSerializer, LineItemSerializer
from django.db import transaction
import random
from customer.serializers import CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    # Define the base queryset to fetch all orders from the database.
    # This queryset is used for GET requests (list and retrieve).
    queryset = Order.objects.all()

    # Specify the serializer that will convert Order objects to JSON and vice versa.
    # This serializer is automatically used in list(), retrieve(), create(), update(), and delete() operations.
    # OrderViewSet does NOT automatically save objects to the database because the create method is overriden.
    serializer_class = OrderDetailSerializer

    # Ensures that all database operations inside the method succeed together.
    # If any operation fails, all changes are rolled back to maintain data consistency.
    @transaction.atomic
    def create(self, request):
        """Handles order creation (equivalent to Java's placeOrder method)."""

        # print("Receive request data:", request.data)

        # Parse request data
        customer_data = request.data.get("customerForm", {})  # Retrieve the entire customer information
        cart_data = request.data.get("cart", {})
        line_items_data = cart_data.get("itemArray", [])  # Retrieve all cart items

        # Deserialize and validate customer data using CustomerSerializer
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer = customer_serializer.save()
        else:
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        confirmation_number = random.randint(100000000, 999999999)

        # Create Order
        order = Order.objects.create(
            amount=0,  # Initially set to 0, will be updated after calculating total amount
            confirmation_number=confirmation_number,
            customer_id=customer.id,  # Use the generated customer_id
        )

        total_amount = 0  # Initialize total amount

        # Create Line Items
        for item in line_items_data:
            book_data = item.get("book", {})  # Retrieve book details
            book_id = book_data.get("bookId")  # Get book ID
            price = book_data.get("price", 0)  # Get price, default to 0
            quantity = item.get("quantity", 1)  # Get quantity, default to 1

            # Accumulate total amount
            total_amount += price * quantity

            book = Book.objects.get(id=book_id)

            # Create LineItem entry
            LineItem.objects.create(
                order=order,
                book_snapshot={
                    "id": book.id,
                    "title": book.title,
                    "price": book.price,
                    "category": book.category.id
                },
                quantity=quantity
            )

        # Update total order amount
        order.amount = total_amount
        order.save()

        # Use two serializers separately, then merge them
        order_basic_data = OrderBasicSerializer(order).data
        order_detail_data = OrderDetailSerializer(order).data

        # Merge the two serialized results into one structured response
        result = {"order": order_basic_data, **order_detail_data}

        return Response(result, status=status.HTTP_201_CREATED)
