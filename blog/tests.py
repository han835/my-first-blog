from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list

class HomePageTest(TestCase):
    def test_root_url_resolves_to_post_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_post_view_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<html>', html)
        self.assertIn('<title>Harry\'s Blog</title>', html)
        self.assertIn('</html>', html)
