from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpRequest
from shop.models import Product
from shop.forms import CustomUserCreationForm, UserAuthForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView


class AllProductsView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    # ordering = ['title']
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["is_authenticated"] = self.request.user.is_authenticated
        return data

# def all_products(request: HttpRequest):
#     current_time = datetime.now()
#     products = Product.objects.all()
#     return render(request, template_name='products.html', context={
#         'current_time': current_time,
#         'products': products,
#         "is_authenticated": request.user.is_authenticated})

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related("productimage_set")
def registration_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_products")
    form = CustomUserCreationForm()
    return render(request, "registration.html", context={"form": form})

class LoginView(View):

    @staticmethod
    def get(request: HttpRequest):
        form = UserAuthForm()
        return render(request, "login.html", context={"form": form})

    @staticmethod
    def post(request: HttpRequest):
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

class RegistrationView(View):
    @staticmethod
    def get(request: HttpRequest):
        form = CustomUserCreationForm()
        return render(request, 'registration.html', context={"form": form})

    @staticmethod
    def post(request: HttpRequest):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("all-products")
        form = CustomUserCreationForm()
        return render(request, 'registration.html', context={"form": form})


# def login_page(request: HttpRequest):
#     if request.method == "POST":
#         form = UserAuthForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("[password")
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect("main-page")
#             else:
#                 messages.error(request, "Неверное имя пользователя или пароль")
#         else:
#             messages.error(request, form.errors)
#
#     form = UserAuthForm()
#     return render(request, "login.html", context={"form": form})

def logout_user(request: HttpRequest):
    logout(request)
    return redirect("main-page")

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related("productimage_set")