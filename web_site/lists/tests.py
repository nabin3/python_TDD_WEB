from django.test import TestCase

class HomePageTest(TestCase):
    # This test is for Django Test Client
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.xhtml')