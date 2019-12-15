from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class CreateAccountViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_happy_path(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'some@email.com',
            'password': 'kajsdf98asudf',
            'colour': 'red',
            'animal': ['bear', ],
            'tiger_type': 'something',
        })

        self.assertEqual(response.status_code, 200)

    def test_bad_email(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'not an email',
            'password': 'kajsdf98asudf',
            'colour': 'red',
            'animal': ['bear', ],
            'tiger_type': 'something',
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'email': ['Enter a valid email address.']})

    def test_bad_password(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'some@email.com',
            'password': 'password',
            'colour': 'red',
            'animal': ['bear', ],
            'tiger_type': 'something',
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'password': ['This password is too common.']})

    def test_bad_colour(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'some@email.com',
            'password': 'kajsdf98asudf',
            'colour': 'not colour',
            'animal': ['bear', ],
            'tiger_type': 'something',
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'colour': ['"not colour" is not a valid choice.']})

    def test_bad_animal(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'some@email.com',
            'password': 'kajsdf98asudf',
            'colour': 'red',
            'animal': ['bear', 'cat'],
            'tiger_type': 'something',
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'animal': ['"cat" is not a valid choice.']})

    def test_bad_tiger_type(self):
        response = self.client.post(reverse('create-account'), {
            'email': 'some@email.com',
            'password': 'kajsdf98asudf',
            'colour': 'red',
            'animal': ['bear', ],
            'tiger_type': '',
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'tiger_type': ['This field may not be blank.']})
