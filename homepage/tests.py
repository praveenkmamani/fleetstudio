from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Basic Testing class for the Profile Model, creates an entry for the user and tests it.
# python manage.py test
class ProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='password')
        testuser1.save()

        test_profile = Profile.objects.create(
            profileUser=testuser1, firstName="praveen", lastName="kumar", emailid="hello@praveen.com", phoneNumber=1234567890)
        test_profile.save()

    def test_profile_data(self):
        profile = Profile.objects.get(id=1)
        profileUser = f'{profile.profileUser}'
        firstName = f'{profile.firstName}'
        lastName = f'{profile.lastName}'
        emailid = f'{profile.emailid}'
        phoneNumber = profile.phoneNumber

        self.assertEqual(profileUser, "testuser1")
        self.assertEqual(firstName, 'praveen')
        self.assertEqual(lastName, 'kumar')
        self.assertEqual(emailid, 'hello@praveen.com')
        self.assertEqual(phoneNumber, 1234567890)