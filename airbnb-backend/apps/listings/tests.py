from django.test import TestCase
from .models import Listing

class ListingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Listing.objects.create(
            title='Test Listing',
            description='A description for the test listing.',
            price=100.00,
            location='Test Location',
            amenities='WiFi, Pool',
            host_id=1
        )

    def test_listing_content(self):
        listing = Listing.objects.get(id=1)
        expected_object_name = f'{listing.title}'
        self.assertEqual(expected_object_name, 'Test Listing')
        self.assertEqual(listing.price, 100.00)
        self.assertEqual(listing.location, 'Test Location')

    def test_listing_str(self):
        listing = Listing.objects.get(id=1)
        self.assertEqual(str(listing), listing.title)