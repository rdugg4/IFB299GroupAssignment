from django.test import TestCase
from django.urls import reverse

class test_createAccount(TestCase):

    def test_indexHTML(self):
        response = self.client.get('/CRC/accounts/')
        self.assertTemplateUsed(response, 'testApp/ShaleenCreateYourAccountPage.html')