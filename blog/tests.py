from django.urls import resolve
from django.test import TestCase
from blog.views import post_list

class HomePageTest(TestCase):
    def test_root_url_resolves_to_post_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)
