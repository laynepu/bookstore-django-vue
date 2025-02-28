from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'category'  # Specify the database table name to prevent Django from adding a prefix

    def __str__(self):
        return f"Category{{name='{self.name}'}}"
