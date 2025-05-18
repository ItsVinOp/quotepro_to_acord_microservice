# test_main.py
import unittest
from main import app
import base64

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {
            'Authorization': 'Basic ' + base64.b64encode(b'admin:password').decode('utf-8'),
            'Content-Type': 'application/json'
        }

    def test_valid_input(self):
        data = {
            "policyNumber": "TEST123",
            "customer": {
                "name": "Test User",
                "email": "test@example.com"
            }
        }

        response = self.client.post("/convert", json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<PolicyNumber>TEST123</PolicyNumber>", response.get_json()["payload"])

if __name__ == '__main__':
    unittest.main()
