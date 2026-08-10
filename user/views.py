from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Userform
from django.urls import reverse_lazy


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = Userform
    template_name = 'user/add_users.html'
    success_url = reverse_lazy('user_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = Userform
    template_name = 'user/update_users.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete_users.html'
    success_url = reverse_lazy('user_list')
