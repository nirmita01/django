from django.shortcuts import render
from .models import Order
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/orders/'


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = '/orders/'


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = '/orders/'