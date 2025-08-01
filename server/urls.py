"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.views import AllProductsView, logout_user, RegistrationView, LoginView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', AllProductsView.as_view(), name="all-products"),
    path('register/', RegistrationView.as_view(), name="register-page"),
    path("login/", LoginView.as_view(), name="login-page"),
    path("logout/", logout_user, name="logout-user"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
