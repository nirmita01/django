from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
)

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='suppliers_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='suppliers_create'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='suppliers_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='suppliers_delete'),
]