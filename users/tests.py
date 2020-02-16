from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import SignUpView
# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "dummy_user",
            email = "dummy_user@email.com",
            password = "testing_dummy_user"
        )

        self.assertEqual(user.username, "dummy_user")
        self.assertEqual(user.email, "dummy_user@email.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_super_user(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username = "dummy_super_user",
            email = "dummy_super_user@email.com",
            password="testing_dummy_super_user"
        )

        self.assertEqual(super_user.username, "dummy_super_user")
        self.assertEqual(super_user.email, "dummy_super_user@email.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)


class SignUpPageTest(TestCase):
    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_uses_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_response_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_SignUpView(self):
        view = resolve(reverse('signup'))
        self.assertEqual(
            view.func.__name__,
            SignUpView.as_view().__name__
        )

    def test_signup_page_contains(self):
        self.assertContains(self.response,'SignUp')

    def test_signup_page_not_contains(self):
        self.assertNotContains(self.response,'LogIn')