from rest_framework import serializers
from OrdersApp.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('item','amount','time','customer')