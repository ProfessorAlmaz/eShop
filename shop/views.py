from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpRequest
from shop.models import Product

def all_products(request: HttpRequest):
    current_time = datetime.now()
    products = Product.objects.all()
    return render(request, template_name='products.html',
        context={'current_time': current_time, 'products': products})
