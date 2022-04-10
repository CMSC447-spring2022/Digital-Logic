from django.test import TestCase


class SignUpViewTest(TestCase):
    def test_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
