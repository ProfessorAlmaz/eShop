from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpRequest
from shop.models import Product
from shop.forms import CustomUserCreationForm, UserAuthForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def all_products(request: HttpRequest):
    current_time = datetime.now()
    products = Product.objects.all()
    return render(request, template_name='products.html', context={
        'current_time': current_time,
        'products': products,
        "is_authenticated": request.user.is_authenticated})

def registration_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_products")
    form = CustomUserCreationForm()
    return render(request, "registration.html", context={"form": form})


def login_page(request: HttpRequest):
    if request.method == "POST":
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("[password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main-page")
            else:
                messages.error(request, "Неверное имя пользователя или пароль")
        else:
            messages.error(request, form.errors)

    form = UserAuthForm()
    return render(request, "login.html", context={"form": form})

def logout_user(request: HttpRequest):
    logout(request)
    return redirect("main-page")