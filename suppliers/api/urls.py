from django.urls import path
from suppliers.api.views import SupplierDetailsAPIView, SupplierListView

urlpatterns = [
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("edit-delete-get-supplier/<int:supplier_id>/", SupplierDetailsAPIView.as_view(), name="supplier-detail"),
]