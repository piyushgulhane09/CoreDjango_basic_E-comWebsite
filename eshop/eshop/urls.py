"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path 
from shop.views import index, category,signup,signupSubmit,login,logout,cart,checkout,order
from django.conf.urls.static import static
from django.shortcuts import render
from shop.middlewares import auth_middleware


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('category/<int:category_id>/', category, name="category"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('logout',logout, name="logout"),
    path('cart',cart,name="cart"),
    path('orders',auth_middleware(order),name="orders"),
    path('checkout',checkout,name="checkout"),
    path('signupSubmit', signupSubmit, name="signupSubmit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

