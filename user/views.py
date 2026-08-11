from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Userform
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def user_list(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 5)
    page_number = request.GET.get("page")
    users = paginator.get_page(page_number)

    return render(request, "user/user_list.html", {"users": users})

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    paginate_by = 5


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
