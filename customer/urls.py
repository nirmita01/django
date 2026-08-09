from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customers_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customers_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customers_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customers_delete'),
]