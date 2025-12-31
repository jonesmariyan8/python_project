from django.test import TestCase
from .models import Booking
from django.utils import timezone

class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            user_id=1,
            listing_id=1,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=2),
            status='confirmed'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user_id, 1)
        self.assertEqual(self.booking.listing_id, 1)
        self.assertEqual(self.booking.status, 'confirmed')

    def test_booking_dates(self):
        self.assertTrue(self.booking.start_date < self.booking.end_date)

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f'Booking {self.booking.id} by User {self.booking.user_id}')