from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="test123"
        )
        cls.post = Post.objects.create(
            title="A title", body="Body content", author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A title")
        self.assertEqual(self.post.body, "Body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A title")
