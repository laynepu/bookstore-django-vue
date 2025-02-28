from django.db import models
from category.models import Category

class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    is_public = models.BooleanField()
    is_featured = models.BooleanField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        db_column='category_id'
    )

    class Meta:
        db_table = 'book'  # Specify the database table name to prevent Django from adding a prefix

    def __str__(self):
        return f"Book{{title='{self.title}', author='{self.author}'}}"
