from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = '/supplier/suppliers/'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = '/supplier/suppliers/'


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier/supplier_confirm_delete.html'
    success_url = '/supplier/suppliers/'