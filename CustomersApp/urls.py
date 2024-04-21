from django.urls import path
from CustomersApp.views import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    path('api/v1/customers', CustomerAPIView.as_view(), name='customer-list'),
    path('api/v1/customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
]
