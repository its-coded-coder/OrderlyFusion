from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer
from .serializer import CustomerSerializer

class CustomerAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_customers(self):
        url = reverse('customer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        url = reverse('customer-list')
        data = {'name': 'Test Customer', 'code': 'ABC123', 'phone': '1234567890', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        customer = Customer.objects.first()
        self.assertEqual(customer.name, 'Test Customer')

class CustomerDetailAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Test Customer', code='ABC123', phone='1234567890', email='test@example.com')

    def test_retrieve_customer(self):
        url = reverse('customer-detail', args=[self.customer.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customer(self):
        url = reverse('customer-detail', args=[self.customer.pk])
        data = {'name': 'Updated Customer'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, 'Updated Customer')

    def test_delete_customer(self):
        url = reverse('customer-detail', args=[self.customer.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(pk=self.customer.pk).exists())