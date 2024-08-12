# core/tests.py
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_patients_by_staff():
    client = APIClient()
    response = client.get(reverse('patients_by_staff', kwargs={'id': 1}))
    assert response.status_code == 200
