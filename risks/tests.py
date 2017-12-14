# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Risk, Field, Choice
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Models test cases
class ModelViewTestCase(TestCase):
    """This class defines the test suite for the data models and the risk data view."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = User.objects.create_user(username="tester")
        self.rogue_user = User.objects.create_user(username="rogue") # rogue will try to access tester's risks
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.risk_name = "Vehicle"
        self.field_name = "Lastname"
        self.option_text = "Comprehensive"
        self.risk = Risk(insurer=self.user, name=self.risk_name)

    def test_risk_model_can_create_a_risk_type(self):
        """Test the Risk model can create a risk."""
        old_count = Risk.objects.count()
        self.risk.save()
        new_count = Risk.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_field_model_can_create_a_field(self):
        """Test the Field model can create a field."""
        old_count = Field.objects.count()
        self.risk.save()
        field = self.risk.field_set.create(type=1, name=self.field_name)
        new_count = Field.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_choice_model_can_create_an_option(self):
        """Test the Choice model can create an options."""
        old_count = Choice.objects.count()
        self.risk.save()        
        field = self.risk.field_set.create(type=4, name=self.field_name)
        option = field.choice_set.create(text=self.option_text)
        new_count = Choice.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_authentication_is_enforced_for_all_and_single_risk_get_requests(self):
        """Test that the api has user authentication."""
        new_client = APIClient()
        self.risk.save()
        risk_get_resp = new_client.get(
            reverse('risk_data',
            kwargs={'pk': self.risk.id}), format="json")
        risks_get_resp = new_client.get("/risks/", format="json")
        self.assertEqual(risk_get_resp.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(risks_get_resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorization_is_enforced_for_single_risk_requests(self):
        """Test that the api has user authorization."""
        new_client = APIClient()

        # try to access user's risk as rogue_user
        new_client.force_authenticate(user=self.rogue_user)
        self.risk.save()
        response = new_client.get(
            reverse('risk_data',
            kwargs={'pk': self.risk.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_correct_risk_list_for_authenticated_user(self):
        """Test the api can get a correct data for a given insurer risk""" 
        self.risk.save()
        risk2 = Risk.objects.create(insurer=self.user, name="House")

        response = self.client.get(
            reverse('risks'), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)      
        self.assertContains(response, '[{"id":3,"name":"Vehicle"},{"id":4,"name":"House"}]')

    def test_api_can_get_correct_sigle_risk_data(self):
        """Test the api can get a correct data for a given insurer risk""" 
        self.risk.save()
        field = self.risk.field_set.create(type=4, name=self.field_name)
        option = field.choice_set.create(text=self.option_text)

        response = self.client.get(
            reverse('risk_data',
            kwargs={'pk': self.risk.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)      
        self.assertContains(response, '{"fields":[{"type":4,"name":"Lastname","options":["Comprehensive"]}],"risk":"Vehicle"}')
