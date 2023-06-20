import unittest
import json
from app import app


class APITestCase(unittest.TestCase):
    def __init__(self):
        self.app = None

    def setUp(self):
        self.app = app.test_client()

    def test_get_posts(self):
        response = self.app.get('/api/posts')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

        if len(data) > 0:
            post = data[0]
            self.assertIn('poster_name', post)
            self.assertIn('poster_avatar', post)
            self.assertIn('pic', post)
            self.assertIn('content', post)
            self.assertIn('views_count', post)
            self.assertIn('likes_count', post)
            self.assertIn('pk', post)

    def test_get_post(self):
        response = self.app.get('/api/posts/1')
        data = json.loads(response.data.decode('utf-8'))

        if response.status_code == 200:
            self.assertIsInstance(data, dict)
            self.assertIn('poster_name', data)
            self.assertIn('poster_avatar', data)
            self.assertIn('pic', data)
            self.assertIn('content', data)
            self.assertIn('views_count', data)
            self.assertIn('likes_count', data)
            self.assertIn('pk', data)
        else:
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data, 'Post not found')


if __name__ == '__main__':
    unittest.main()
