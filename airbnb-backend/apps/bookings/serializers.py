from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'user', 'listing', 'start_date', 'end_date', 'status']