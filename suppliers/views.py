from django.shortcuts import render
from .models import Supplier
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SupplierForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def supplier_list(request):
    suppliers_list = Supplier.objects.all()
    paginator = Paginator(suppliers_list, 5)
    page_number = request.GET.get("page")
    suppliers = paginator.get_page(page_number)

    return render(request, "suppliers/supplier_list.html", {"suppliers": suppliers})


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/create_supplier.html'
    success_url = reverse_lazy('supplier_list')


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/update_supplier.html'
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/delete_supplier.html'
    success_url = reverse_lazy('supplier_list')
