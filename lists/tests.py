from django.test import TestCase, Client
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
import re

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        
        response = self.client.get('/')
        html = re.sub('\s+',' ',response.content.decode('utf8')).strip()
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title> To-Do lists </title>', html)
        self.assertTrue(html.endswith('</html>'))
        
        self.assertTemplateUsed(response, 'home.html')
