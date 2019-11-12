from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTEst(TestCase):

    def test_create_user_with_email_successful(self):
        """Create a new user with email ok"""
        email = 'test@jesusnoseq.com'
        password = 'abcd1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = "test@JESUSNOSEQ.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@jesusnoseq.com',
            'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
