import unittest
from app import app, fetch_news

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a Flask test client
        self.app = app.test_client()
        self.app.testing = True

    # Test that the index page loads successfully
    def test_index_page_loads(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    # Test fetching news with a valid API key
    def test_fetch_news(self):
        articles, total_results = fetch_news(page=1, page_size=4)
        self.assertIsInstance(articles, list)
        self.assertGreaterEqual(total_results, 0)

    # Test missing API key error
    def test_missing_api_key(self):
        # Temporarily remove API key
        app.config['NEWS_API_KEY'] = None
        with self.assertRaises(Exception) as context:
            fetch_news(page=1, page_size=4)
        self.assertIn("API key is missing", str(context.exception))

if __name__ == "__main__":
    unittest.main()
