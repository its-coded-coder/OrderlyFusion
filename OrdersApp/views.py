import asyncio
import africastalking
from os import environ
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from OrdersApp.models import Order
from OrdersApp.serializer import OrderSerializer

class OrdersAPIView(APIView):
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

    async def send_sms_async(self, message):
        africastalking.initialize(environ.get("AFRICAS_TALKING_USERNAME"), environ.get("AFRICAS_TALKING_API_KEY"))
        await asyncio.sleep(0)  # Simulate asynchronous operation
        africastalking.SMS.send(message, ["+254715592073"])

class OrderDetailAPIView(APIView):
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