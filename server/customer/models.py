from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError

def validate_name_length(value):
    """Custom validator to check name length and provide a message."""
    if len(value) < 4 or len(value) > 45:
        raise ValidationError("Name must be between 4 and 45 characters.")

class Customer(models.Model):
    """ Represents a customer with personal and payment information """
    name = models.CharField(
        max_length=45,
        validators=[validate_name_length],  # Use the custom validator
    )
    address = models.TextField()
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r"^((\(\d{3}\))|\d{3})[- .]?\d{3}[- .]?\d{4}$|^\d{10}$", message="Invalid phone number format. Allowed formats: (XXX)XXX-XXXX, XXX-XXX-XXXX, XXX.XXX.XXXX, XXX XXX XXXX, XXXXXXXXXX")]
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Invalid email format.")]
    )
    cc_number = models.CharField(max_length=16)  # Masking should be handled in the frontend
    cc_expiry_month = models.IntegerField()
    cc_expiry_year = models.IntegerField()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.name} ({self.email})"
