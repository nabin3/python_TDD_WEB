from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heared about this cool new online to-do app
        # She goes to check out it's homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is ivited to insert a to-do item straight away.
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        # (Edith hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in to do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

        # There is still a text box inviting to add another item
        # She enters "Use peacock feather to make a fly"(Edith is very methodical)
        self.fail('Fininsh the test!')

        # The page update again, and now shows both item on her list

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()