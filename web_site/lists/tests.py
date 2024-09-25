from django.test import TestCase

class HomePageTest(TestCase):
    # This test is for Django Test Client
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.xhtml')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertContains(response, 'A new list item')
        self.assertTemplateUsed(response, 'home.xhtml')