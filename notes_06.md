* Django's ```LiveServerTestCase``` class creates a test database and startup a development server for the functional tests to run against. 
* ```git mv``` is used to keep tarck of the fact that the file which is moved by this command should have single history.
* impllicit wait is off by default in selenium(they are discouraged) so we explicit wait by time.sleep(), but if we wait for like 1 sec then our FT will get slow and if we do wait only for 0.1 sec then we get use Unexpected errors like NoSuchElementException and StaleElementException errors are often a sign that you need to wait until the page load properly.
```bash
[...]
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 5

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        [...]
    def tearDown(self):
        [...]

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time() 
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)
```