from rest_framework import serializers
from .models import Order, LineItem
from customer.models import Customer

class OrderBasicSerializer(serializers.ModelSerializer):
    orderId = serializers.IntegerField(source="id")
    customerId = serializers.IntegerField(source="customer.id")
    dateCreated = serializers.DateTimeField(source="date_created")  # Convert to camelCase
    confirmationNumber = serializers.IntegerField(source="confirmation_number")  # Convert to camelCase

    class Meta:
        model = Order
        fields = ["orderId", "amount", "dateCreated", "confirmationNumber", "customerId"]

class LineItemSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField()
    orderId = serializers.IntegerField(source="order.id", read_only=True)

    class Meta:
        model = LineItem
        fields = ["bookId", "orderId", "quantity"]

    def get_bookId(self, obj):
        """ Safely retrieves book ID from the snapshot if it exists """
        return obj.book_snapshot.get('id') if obj.book_snapshot else None

class CustomerSerializer(serializers.ModelSerializer):
    """ Serializer for the Customer model to include customer details in OrderSerializer. Excludes sensitive credit card information. """
    maskedCCNumber = serializers.SerializerMethodField() # Currently implemented for credit card only.
    ccExpDate = serializers.SerializerMethodField()  # Return formatted expiration date

    class Meta:
        model = Customer
        fields = ["name", "address", "phone", "email", "maskedCCNumber", "ccExpDate"]  # Exclude credit card details from frontend response.

    def get_maskedCCNumber(self, obj):
        """ Returns a masked credit card number (only first 2 and last 4 digits visible) """
        if obj.cc_number:
            return f"{obj.cc_number[:2]}** **** **** {obj.cc_number[-4:]}"  # Shows only partial CC number
        return "No Credit Card on File"

    def get_ccExpDate(self, obj):
        """ Returns the expiration date in YYYY-MM-DD format """
        if obj.cc_expiry_month and obj.cc_expiry_year:
            return f"{obj.cc_expiry_year}-{obj.cc_expiry_month:02d}-01"  # Ensure leading zero in month
        return None

class BookSerializer(serializers.Serializer):
    """ Serializer for extracting book details from LineItem.book_snapshot """
    bookId = serializers.IntegerField(source="id")
    title = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()

class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed order information, including customer and line items.

    This serializer relies on the following relationships:
    - `Order` → `Customer` (ForeignKey)
    - `Order` → `LineItem` (One-to-Many)

    Since `Order` has direct relationships with `Customer` and `LineItem`, DRF can automatically retrieve their data.
    If there were no direct relationships (Book), we would need to use `SerializerMethodField` to manually fetch related data.
    """
    customer = CustomerSerializer(read_only=True)
    lineItems = LineItemSerializer(many=True, read_only=True, source="line_items") # source="line_items" is required because the related_name on the ForeignKey determines the returned field name as 'line_items'

    books = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["customer", "books", "lineItems"]

    def get_books(self, obj):
        """
        Retrieves book details from the `book_snapshot` field in each `LineItem`.
        This ensures that the book details reflect the state of the book at the time of purchase,
        rather than fetching the latest data from the `Book` model.
        """
        books = [item.book_snapshot for item in obj.line_items.all() if item.book_snapshot]
        return BookSerializer(books, many=True).data # Serializes the stored book snapshot data
