import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heared about this cool new online to-do app
        # She goes to check out it's homepage.
        self.browser.get('http://localhost:8000')

        # She noticed the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is ivited to insert a to-do item straight away.
        self.fail('Finish the test!')

        # She types "Buy peacock feathers" into a text box
        # (Edith hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in to do list

        # There is still a text box inviting to add another item
        # She enters "Use peacock feather to make a fly"(Edith is very methodical)

        # The page update again, and now shows both item on her list

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()