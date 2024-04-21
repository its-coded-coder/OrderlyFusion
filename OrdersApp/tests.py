from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

from OrdersApp.models import Order
from OrdersApp.serializer import OrderSerializer
from OrdersApp.views import OrdersAPIView, OrderDetailAPIView
from CustomersApp.models import Customer  # Import Customer model

class OrdersAPIViewTestCase(APITestCase):
    def setUp(self):
        self.client = Client()
        # Create a customer
        self.customer = Customer.objects.create(name='Test Customer', email='test@example.com')

    def test_get_orders(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        data = {
            'customer': self.customer.id,  # Link the order to the created customer
            'order_field': 'value'  # Add other fields as required by your Order model
        }
        response = self.client.post('/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderDetailAPIViewTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(order_field='value')  # Add your order data here
        self.client = Client()

    def test_get_order(self):
        response = self.client.get(f'/orders/{self.order.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        data = {'order_field': 'updated_value'}  # Add updated order data here
        response = self.client.put(f'/orders/{self.order.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(f'/orders/{self.order.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SendSMSAsyncTestCase(TestCase):
    @patch('africastalking.SMS.send')
    def test_send_sms_async(self, mock_send):
        message = "Test Message"
        order_view = OrdersAPIView()
        order_view.send_sms_async(message)
        mock_send.assert_called_once_with(message, ["+254715592073"])
