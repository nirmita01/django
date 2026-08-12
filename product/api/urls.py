from django.urls import path
from product.api.views import ProductDetailsAPIView, ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("edit-delete-get-product/<int:product_id>/", ProductDetailsAPIView.as_view(), name="product-detail"),
]