# SignUpTest from https://stackoverflow.com/questions/57337720/writing-django-signup-form-tests-for-checking-new-user-creation

from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class SignUpViewTest(TestCase):
    def test_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)


class DeleteUserViewTest(TestCase):
    def test_delete_user_page(self):
        response = self.client.get('/accounts/delete_account/')
        self.assertEqual(response.status_code, 302)


class SignUpTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'digitallogic'

    def tearDown(self):
        user = authenticate(username='testuser', password='digitallogic')
        user.delete()

    def test_signup_form(self):
        response = self.client.post('/accounts/signup/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


class DeleteUserTest(TestCase):
    def test_delete_get(self):
        user = get_user_model().objects.create_user(username='test', password='123abc456', email='test@example.com')
        user.save()
        response = self.client.post('/accounts/delete_account/')
        self.assertIs()


