from django.urls import path
from OrdersApp import views

urlpatterns = [
    path('order', views.ordersApi, name='order_list'),
    path('order/<int:order_id>/', views.ordersApi, name='order_detail'),
]
