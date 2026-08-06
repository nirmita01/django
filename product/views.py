from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product
from .forms import CategoryForm, ProductForm

# -------------------- Category --------------------

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'product/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/product/categories/'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = '/product/categories/'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/product/categories/'

# -------------------- Product --------------------

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = '/product/products/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = '/product/products/'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/product/products/'