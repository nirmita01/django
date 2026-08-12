from django.urls import path
from customer.api.views import CustomerDetailsAPIView, CustomerListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("edit-delete-get-customer/<int:customer_id>/", CustomerDetailsAPIView.as_view(), name="customer-detail"),
]