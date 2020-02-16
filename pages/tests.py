from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView



class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        
    
    def test_homepage_url_resolves_HomePageView(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_homepage_response_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_contains_html(self):
        self.assertContains(self.response, 'Home Page')

    def test_homepage_does_not_contain(self):
        self.assertNotContains(self.response, "Hello World")

    def test_homepage_uses_template(self):
        self.assertTemplateUsed(self.response, 'home.html')