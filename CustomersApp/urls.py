from django.urls import path
from CustomersApp.views import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    path('customers', CustomerAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
]
