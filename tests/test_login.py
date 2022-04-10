# tests from https://mkdev.me/en/posts/how-to-cover-django-application-with-unit-tests

from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123abc456', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='123abc456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='123abc')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class SignInViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123abc456', email='test@example.com')

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('/login/', {'username': 'test', 'password': '123abc456'})
        self.assertTrue(response.data['authenticated'])

    def test_wrong_username(self):
        response = self.client.post('/login/', {'username': 'wrong', 'password': '123abc456'})
        self.assertFalse(response.data['authenticated'])

    def test_wrong_pssword(self):
        response = self.client.post('/login/', {'username': 'test', 'password': 'wrong'})
        self.assertFalse(response.data['authenticated'])