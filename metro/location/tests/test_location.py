"""Locations tests."""

# Django
import json
from django.test import TestCase

# Django REST Framework
from rest_framework import status

# Models
from metro.location.models import District, Unit

# Serializers
from metro.location.serializers import (DistrictsModelSerializer, 
                                        UnitModelSerializer)

class DistrictTestCase(TestCase):
    def setUp(self):
        """will create a new object and get 
        a list of object to compare"""
        self.district = District.objects.create(
            id=1,
            name="Coyoacán"
        )
        self.districts = District.objects.all()
        # URLs
        self.list_url = '/api/district/'
        self.retrive_url = '/api/district/{}/'.format(
            self.district.id
        )

    def test_response_list_success(self):
        """Verify request succeed."""
        request = self.client.get(self.list_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        # Compare content data
        self.assertEqual(json.loads(request.content), 
        DistrictsModelSerializer(self.districts, many=True).data)

    def test_response_retrive_success(self):
        """Verify request succeed."""
        request = self.client.get(self.retrive_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        # Compare content data
        self.assertEqual(json.loads(request.content), 
        DistrictsModelSerializer(self.district).data)

class UnitTestCase(TestCase):
    def setUp(self):
        self.district = District.objects.create(
            id=1,
            name="Coyoacán"
        )
        self.unit = Unit.objects.create(
            id=1,
            latitude=19.38990020751953,
            longitude=-99.05889892578124,
            district=self.district
        )

        self.unit_test = Unit.objects.get(id=1)
        self.units = Unit.objects.all()
        #URLs
        self.list_url = '/api/unit/'
        self.retrive_url = '/api/district/{}/unit_list/'.format(
            self.unit.id
        )

    def test_response_list_success(self):
        """Verify request succeed."""
        request = self.client.get(self.list_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        # Compare content data
        self.assertEqual(json.loads(request.content), 
        UnitModelSerializer(self.units, many=True).data)

    def test_response_retrive_success(self):
        """Verify request succeed."""
        request = self.client.get(self.retrive_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
