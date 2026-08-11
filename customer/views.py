from django.shortcuts import render
from .models import Customer
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomerForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def customer_list(request):
    customers_list = Customer.objects.all()
    paginator = Paginator(customers_list, 5)
    page_number = request.GET.get("page")
    customers = paginator.get_page(page_number)

    return render(request, "customer/customer_list.html", {"customers": customers})

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 5

    
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/add_customer.html'
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/update_customer.html'
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('customer_list')
