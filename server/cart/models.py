from django.db import models
from book.models import Book

class ShoppingCart(models.Model):
    surcharge = models.IntegerField(default=500)

    class Meta:
        db_table = 'shopping_cart'

    # `items` is not explicitly defined in this model,
        # but Django automatically creates it as a reverse relation
        # from `ShoppingCartItem` due to `related_name="items"`.
    def computed_subtotal(self):
        """
        Calculate the total price of all items in the shopping cart (excluding surcharge).
        """
        return sum(item.quantity * item.book.price for item in self.items.all())

    def __str__(self):
        return f"ShoppingCart {self.id}"


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'shopping_cart_item'

    def get_book_id(self):
        return self.book.id

    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Cart {self.cart.id}"