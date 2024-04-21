from django.urls import path
from OrdersApp import views

urlpatterns = [
    path('orders/', views.OrdersAPIView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='order_detail'),
]
