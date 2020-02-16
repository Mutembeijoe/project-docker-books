from django.test import TestCase
from django.contrib.auth import get_user_model

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

