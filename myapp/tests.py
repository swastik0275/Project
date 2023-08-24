from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='swastik@example.com',
            password='testpassword',
            first_name='Swastik',
            last_name='kalyane'
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, 'swastik@example.com')
        self.assertEqual(self.user.first_name, 'Swastik')
        self.assertEqual(self.user.last_name, 'kalyane')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            email='skalyane@example.com',
            password='adminpassword',
            first_name='swastik',
            last_name='kalyane'
        )
        self.assertEqual(superuser.email, 'skalyane@example.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_str_representation(self):
        self.assertEqual(str(self.user), 'swastik@example.com')

    # Add more test cases as needed

# Add more test classes if you have more models or components to test
