from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from shop.models import Product

def all_products(request: HttpRequest):
    products = Product.objects.all()
    return render(request, template_name='products.html',
        context={'products': products})
