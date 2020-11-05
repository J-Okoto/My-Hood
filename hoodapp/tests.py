

from django.test import TestCase
from .models import neighbourhood,Profile
from django.contrib.auth.models import User

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(
            name='Emba')
        self.hood.save_Neighbourhood()

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

        # Testing Save Method
    def test_save_method(self):
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.hood.delete_Neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(name="Emba")
        self.neighbourhood.save()
        self.user = Profile(name='Joel', email='okotojr@gmail.com', neighbourhood=self.neighbourhood,
                                 username="Joe", description="Cool&Calm")
        self.user.save_User()

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,Profile))

        # Testing Save Method
    def test_save_method(self):
        user =Profile.objects.all()
        self.assertTrue(len(user) > 0)

    def test_delete_method(self):
        self.user.delete_User()
        user =Profile.objects.all()
        self.assertTrue(len(user) == 0)
