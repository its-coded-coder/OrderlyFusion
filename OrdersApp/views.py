import africastalking 
from decouple import config
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from OrdersApp.models import Order
from OrdersApp.serializer import OrderSerializer

@csrf_exempt
def ordersApi(request,id=0):
    if request.method=='GET':
        
        listAllOrders = Order.objects.all()
      
        orders_serializer=OrderSerializer(listAllOrders,many=True)

        return JsonResponse(orders_serializer.data,safe=False)
    
    elif request.method=='POST':
      
        order_data=JSONParser().parse(request)
        
        orders_serializer=OrderSerializer(data=order_data)
        
        if orders_serializer.is_valid():
        
            orders_serializer.save()
            
            # Initialize africa talking sms SDK
            africastalking.initialize(config("AFRICAS_TALKING_USERNAME"), config("AFRICAS_TALKING_API_KEY"))

            # Use the service synchronously
            response = africastalking.SMS.send("Hello Message!", ["+254715592073"])

            return JsonResponse("Order Added Successfully",safe=False)

        
        return JsonResponse("Failed to Add Order",safe=False)
    
    elif request.method=='PUT':

        order_data=JSONParser().parse(request)
        
        order = Order.objects.get(OrderId=order_data['id'])
        
        orders_serializer=OrderSerializer(order,data=order_data)
        
        if orders_serializer.is_valid():
        
            orders_serializer.save()
        
            return JsonResponse("Updated Successfully",safe=False)
        
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
    
        order=Order.objects.get(OrderId=id)
    
        order.delete()
    
        return JsonResponse("Deleted Successfully",safe=False)
