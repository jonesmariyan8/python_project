from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Review
from django.contrib.auth import get_user_model

User = get_user_model()

class ReviewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.review_data = {
            'rating': 5,
            'comment': 'Great place!',
            'user': self.user.id,
        }
        self.review = Review.objects.create(**self.review_data)

    def test_create_review(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('review-list'), self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

    def test_get_review(self):
        response = self.client.get(reverse('review-detail', args=[self.review.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], self.review.comment)

    def test_update_review(self):
        self.client.login(username='testuser', password='testpass')
        updated_data = {'rating': 4, 'comment': 'Good place!'}
        response = self.client.put(reverse('review-detail', args=[self.review.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 4)

    def test_delete_review(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('review-detail', args=[self.review.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)