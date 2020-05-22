from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_look_at_cv(self):
        # I want to look at my website.
        # I go to go check out the cv.
        self.browser.get('http://127.0.0.1:8000/cv')

        # I should be able to view all posts initially.
        # I should be able to view a post in detail.
        # I should be able to edit a post.
        # I should be able to create a post.

        # The title should mention my name.
        self.assertIn('Harry', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
