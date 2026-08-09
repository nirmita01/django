from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.hashers import make_password
from orders.models import Order
from django.db.models import Count
from product.models import Product

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = UserLoginForm()

    return render(request, "home/login.html", {"form": form})


def Signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created succesfully. Please log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/signup.html', {'form': form})


def dashboard_view(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    context = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_products': total_products,
    }
    return render(request, 'home/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')