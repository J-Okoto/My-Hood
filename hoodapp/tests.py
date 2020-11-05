

from django.test import TestCase
from .models import neighbourhood
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Emba = neighbourhood(neighbourhood='Emba')

    def test_instance(self):
        self.assertTrue(isinstance(self.Emba,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Emba.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Emba.delete_neighbourhood('Emba')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

