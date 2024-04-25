# views.py
import asyncio
import africastalking
from os import environ
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from OrdersApp.models import Order, Customer
from OrdersApp.serializer import OrderSerializer, CustomerSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions

class OrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.send_sms_async("Order Added Successfully")
            return Response("Order Added Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_sms(self, message):
        try:
            africastalking.initialize(environ.get("AFRICAS_TALKING_USERNAME"), environ.get("AFRICAS_TALKING_API_KEY"))
            africastalking.SMS.send(message, ["+254715592073"])
        except Exception as e:
            print(f"Error sending SMS: {e}")

class OrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if order:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        order = self.get_object(pk)
        if order:
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        order = self.get_object(pk)
        if order:
            order.delete()
            return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)
        return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

# Obtain token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# Customer List View
class CustomerListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)