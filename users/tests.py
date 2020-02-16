from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
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
    username = 'savitar'
    email = 'savitar@email.com'

    def setUp(self):
        url =reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertTrue(self.response.status_code, 200)
        self.assertContains(self.response, 'SignUp')
        self.assertNotContains(self.response, 'Hello World')


    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email, 'hesoyam')

        self.assertEqual(get_user_model().objects.all().count(), 1)

        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)

        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)