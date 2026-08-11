from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy

def product_list(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 5)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "product/product_list.html", {"products": products})


# -------------------- Category --------------------

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'product/category_list.html'
    context_object_name = 'categories'
    paginate_by = 5


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/create_category.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/update_category.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'product/delete_category.html'
    success_url = reverse_lazy('category_list')


# -------------------- Product --------------------

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 5


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('products_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('products_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('products_list')