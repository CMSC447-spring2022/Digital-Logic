import json

from django.test import TestCase
from Launcher.clients import LauncherClient


# Client tests
class TestLauncherClient(TestCase):
    def setUp(self):
        LauncherClient()

    def test_request_and_destroy_container(self):
        res = LauncherClient.request_container()
        self.assertEqual(res.status_code, 200)
        text = json.loads(res.text)['username']
        self.assertEqual('user@kasm.local', text)

        container_id = json.loads(res.text)['kasm_id']
        res = LauncherClient.destroy_container(container_id)
        self.assertEqual(200, res.status_code)

    def test_request_failure(self):
        res = LauncherClient.request_container()
        self.assertEqual(res.status_code, 200)
        text = json.loads(res.text)['username']
        self.assertEqual('user@kasm.local', text)

        res2 = LauncherClient.request_container()
        self.assertEqual(res2.status_code, 200)
        error_text = json.loads(res2.text)['error_message']
        self.assertEqual('No resources are available to create the requested Kasm. Please try again later or contact an Administrator', error_text)

        container_id = json.loads(res.text)['kasm_id']
        res = LauncherClient.destroy_container(container_id)
        self.assertEqual(res.status_code, 200)
