from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class VisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

class NewVisitorTest(VisitorTest):

    def test_can_look_at_blog(self):
        # Rachael wants to look at Harry's
        # website. She goes to check it out.
        self.browser.get('http://127.0.0.1:8000')
        time.sleep(3)

        # Rachael then checks she is in the
        # right place by looking at the title
        # and header.
        self.assertIn('Harry\'s Blog', self.browser.title)
        self.assertIn('Harry Neil', self.browser.find_element_by_tag_name('h1').text)

class CvReaderTest(VisitorTest):

    def test_can_look_at_cv(self):
        # John wants to check out Harry's CV page.
        # He goes to check the page out.
        self.browser.get('http://127.0.0.1:8000/cv')
        time.sleep(3)

        # He is met with a page displaying Harry's CV.
        # The CV page contains a header with information
        # about Harry.
        self.assertIn('Harry', self.browser.title)

        # Collecting all h2 elements and putting them into 1 string.
        header2Collection = self.browser.find_elements_by_tag_name('h2')
        header2Text = ""

        for header in header2Collection:
            header2Text = header2Text + header.text

        # The CV page contains an education section.
        self.assertIn('Education', header2Text)

        # The CV page contains an experience section.
        self.assertIn('Experience', header2Text)

        # The CV page contains information about Harry's
        # skills and interests.
        self.assertIn('Skills', header2Text)
        self.assertIn('Interests', header2Text)

        # The CV page contains information about awards.
        self.assertIn('Awards', header2Text)

    def test_can_access_cv_from_home_page(self):
        # John wants to look at Harry's CV.
        # He first checks out Harry's page.
        self.browser.get('http://127.0.0.1:8000')
        time.sleep(3)

        # He then finds the link to the CV page.
        link = self.browser.find_element_by_link_text('CV')
        link.click()

        # He checks that the correct url is found.
        self.assertEqual('http://127.0.0.1:8000/cv/', self.browser.current_url)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
