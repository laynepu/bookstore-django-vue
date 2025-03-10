from django.db import models
from customer.models import Customer

class Order(models.Model):
    """ Represents a customer order """
    amount = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confirmation_number = models.BigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order {self.id} (Customer {self.customer.id})"

class LineItem(models.Model):
    """ Represents an item in an order """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="line_items")
    book_snapshot = models.JSONField()  # Store book data as a snapshot to ensure historical accuracy in orders
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order_line_item'

    def __str__(self):
        return f"Book {self.book_id} x {self.quantity} (Order {self.order.id})"