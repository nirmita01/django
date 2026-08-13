from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Order
from .forms import OrderForm
from rest_framework.permissions import IsAuthenticated

def order_list(request):
    orders_list = Order.objects.all()
    paginator = Paginator(orders_list, 5)
    page_number = request.GET.get("page")
    orders = paginator.get_page(page_number)

    return render(request, "order/order_list.html", {"orders": orders})


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/order_list.html"
    context_object_name = "orders"
    paginate_by = 5


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order/create_order.html"
    success_url = reverse_lazy("order_list")


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "order/update_order.html"
    success_url = reverse_lazy("order_list")


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "order/delete_order.html"
    success_url = reverse_lazy("order_list")