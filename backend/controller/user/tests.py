from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='foo')
        self.assertEqual(user.email, 'test@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('admin@user.com', 'foo')
        self.assertEqual(admin_user.email, 'admin@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='admin@user.com', password='foo', is_superuser=False)

class UserViewSetTests(APITestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Linus',
            'last_name': 'Torvalds',
            'email': 'linus@torvalds.com',
            'password': 'linux'
        }

    def test_perform_create(self):
        response = self.client.post(reverse('user-list'), data=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.data, dict)

    def test_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve(self):
        response = self.client.get(reverse('user-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update(self):
        response = self.client.put(reverse('user-detail', args=[1], kwargs={}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update(self):
        response = self.client.patch(reverse('user-detail', args=[1], kwargs={}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_destroy(self):
        response = self.client.delete(reverse('user-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)