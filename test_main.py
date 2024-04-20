import unittest
import json
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'This code has been tested before being deployed, and Render has deployed it automatically.')

    def test_get_characters_of_image(self):
        # This test assumes that you have a sample image file named "test_image.png"
        with open('test_image.png', 'rb') as f:
            response = self.app.post('/get_characters_of_image', data={'image': f})
            data = json.loads(response.data.decode('utf-8'))
            print(data)
            self.assertIn('characters', data)
            # Add more assertions based on the expected behavior of your endpoint

if __name__ == '__main__':
    unittest.main()