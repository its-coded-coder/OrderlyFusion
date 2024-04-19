from django.urls import path
from CustomersApp import views

urlpatterns = [
    path('customer', views.customersApi),
    path('department/<int:department_id>', views.customersApi)
]
