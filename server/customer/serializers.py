from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Customer
from datetime import datetime
from calendar import monthrange

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_internal_value(self, data):
        """
        Maps field names from request to model field names.
        """
        data = data.copy()  # Avoid modifying the original data
        if 'ccNumber' in data:
            data['cc_number'] = data.pop('ccNumber')
        if 'ccExpiryMonth' in data:
            data['cc_expiry_month'] = int(data.pop('ccExpiryMonth'))
        if 'ccExpiryYear' in data:
            data['cc_expiry_year'] = int(data.pop('ccExpiryYear'))
        return super().to_internal_value(data)

    def validate_address(self, value):
        if not value or len(value) < 4 or len(value) > 45:
            raise ValidationError("Address must be between 4 and 45 characters.")
        return value

    def validate_cc_number(self, value):
        if not value:
            raise ValidationError("Credit card number cannot be empty.")
        cleaned_number = ''.join(filter(str.isdigit, value))
        if len(cleaned_number) < 14 or len(cleaned_number) > 16:
            raise ValidationError("Credit card number must be between 14 and 16 digits.")
        return cleaned_number

    def validate(self, data):
        month = data.get('cc_expiry_month')
        year = data.get('cc_expiry_year')

        if not month or not year:
            raise ValidationError("Expiry month and year are required.")

        if month < 1 or month > 12:
            raise ValidationError("Expiry month must be between 1 and 12.")

        try:
            # Get the last day of the given month
            last_day_of_month = monthrange(year, month)[1]
            expiry_date = datetime(year, month, last_day_of_month, 23, 59, 59) # Set to the last second of the last day
            now = datetime.now()

            if expiry_date < now:
                raise ValidationError("Credit card has expired.")

            if year < now.year or year > now.year + 20:
                raise ValidationError("Expiry year must be within the next 20 years.")
        except ValueError:
            raise ValidationError("Invalid expiry month or year.")

        return data