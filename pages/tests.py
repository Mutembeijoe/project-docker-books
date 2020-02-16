from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView



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


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_contains_html(self):
        self.assertContains(self.response, 'About Page')

    def test_about_page_does_not_contain_html(self):
        self.assertNotContains(self.response, 'What page is this?')

    def test_about_page_resolves_AboutPageView(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)