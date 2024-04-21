from rest_framework import serializers
from OrdersApp.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('id','item','amount','time','customer')