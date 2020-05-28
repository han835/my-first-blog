from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User

from blog.views import post_list, cv_detail, cv_edit

from blog.models import Cv

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

    def test_post_new_authentication(self):
        response = self.client.get('/post/new/')
        self.assertTrue(response.status_code, 401)

    def test_post_draft_list_authentication(self):
        response = self.client.get('/drafts/')
        self.assertTrue(response.status_code, 401)

class CvPageTest(TestCase):

    def test_cv_url_resolves_to_cv_detail(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_detail)

    def test_cv_detail_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv_detail.html')

class CvModelTest(TestCase):

    def test_saving_and_retrieving_cv(self):
        me = User()
        me.username = 'test'
        me.save()

        first_cv = Cv()
        first_cv.author = me
        first_cv.header = 'Header1'
        first_cv.education = 'Education1'
        first_cv.experience = 'Experience1'
        first_cv.skills_interests = 'Skills/Interests1'
        first_cv.awards = 'Awards1'
        first_cv.save()

        second_cv = Cv()
        second_cv.author = me
        second_cv.header = 'Header2'
        second_cv.education = 'Education2'
        second_cv.experience = 'Experience2'
        second_cv.skills_interests = 'Skills/Interests2'
        second_cv.awards = 'Awards2'
        second_cv.save()

        saved_cvs = Cv.objects.all()
        self.assertEqual(saved_cvs.count(), 2)

        first_saved_cv = saved_cvs[0]
        second_saved_cv = saved_cvs[1]
        self.assertEqual(first_saved_cv.education, 'Education1')
        self.assertEqual(second_saved_cv.education, 'Education2')

class CvPageEditTest(TestCase):

    def test_cv_edit_url_resolves_to_cv_edit(self):
        found = resolve('/cv/edit/')
        self.assertEqual(found.func, cv_edit)

    def test_cv_edit_authentication(self):
        response = self.client.get('/cv/edit/')
        self.assertTrue(response.status_code, 401)
