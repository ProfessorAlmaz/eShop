from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpRequest
from shop.models import Product
from shop.forms import CustomUserCreationForm

def all_products(request: HttpRequest):
    current_time = datetime.now()
    products = Product.objects.all()
    return render(request, template_name='products.html', context={
        'current_time': current_time,
        'products': products,
        "is_authenticated": request.user.is_authenticated})

def register_page(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_products")
    form = CustomUserCreationForm()
    return render(request, "registration.html", context={"form": form})