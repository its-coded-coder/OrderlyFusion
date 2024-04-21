from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from CustomersApp.models import Customer
from CustomersApp.serializer import CustomerSerializer

class CustomerAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Customer added successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None

    def get(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated successfully")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            customer.delete()
            return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)
