from django.urls import path
from OrdersApp import views

urlpatterns = [
    path('api/v1/orders', views.OrdersAPIView.as_view(), name='order_list'),
    path('api/v1/orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='order_detail'),
]
