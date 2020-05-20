from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_look_at_blog(self):
        # I want to look at my website.
        # I go to check it out.
        self.browser.get('http://127.0.0.1:8000')

        # I should be able to view all posts initially.
        # I should be able to view a post in detail.
        # I should be able to edit a post.
        # I should be able to create a post.

        # The title should mention my name.
        self.assertIn('Harry', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
