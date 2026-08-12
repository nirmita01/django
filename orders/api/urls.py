from django.urls import path
from orders.api.views import OrderDetailsAPIView, OrderListView

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("edit-delete-get-order/<int:order_id>/", OrderDetailsAPIView.as_view(), name="order-detail"),
]