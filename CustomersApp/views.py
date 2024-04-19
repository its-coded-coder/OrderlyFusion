from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CustomersApp.models import Customer
from CustomersApp.serializer import CustomerSerializer

@csrf_exempt
def customersApi(request,id=0):
    if request.method=='GET':
        
        listAllCustomers = Customer.objects.all()
        
        customer_serializer=CustomerSerializer(listAllCustomers,many=True)

        return JsonResponse(customer_serializer.data,safe=False)
    
    elif request.method=='POST':

        customer_data=JSONParser().parse(request)
        
        customer_serializer=CustomerSerializer(data=customer_data)
        
        if customer_serializer.is_valid():
        
            customer_serializer.save()
        
            return JsonResponse("Customer Added Successfully",safe=False)
        
        return JsonResponse("Failed to Add Customer",safe=False)
    
    elif request.method=='PUT':

        customer_data=JSONParser().parse(request)
        
        customer = Customer.objects.get(CustomerId=customer_data['id'])
        
        customer_serializer=CustomerSerializer(customer,data=customer_data)
        
        if customer_serializer.is_valid():
        
            customer_serializer.save()
        
            return JsonResponse("Updated Successfully",safe=False)
        
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
    
        customer=Customer.objects.get(CustomerId=id)
    
        customer.delete()
    
        return JsonResponse("Deleted Successfully",safe=False)