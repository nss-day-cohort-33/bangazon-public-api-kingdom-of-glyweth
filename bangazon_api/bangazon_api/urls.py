"""bangazon_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from bangazon.models import Customer, Order_Products, Order, Payment, Product_Category, Product
from bangazon.views import register_user, login_user
from bangazon.views import Customers
from bangazon.views import Orders
from bangazon.views import Payments
from bangazon.views import Products
from bangazon.views import Order_Products_2
from bangazon.views import Product_Categories

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', Products, 'product')
router.register(r'payment', Payments, 'payment')
router.register(r'customer', Customers, 'customer')
router.register(r'order_product', Order_Products_2, 'order_product')
router.register(r'order', Orders, 'order')
router.register(r'product_category', Product_Categories, 'product_category')
router.register(r'product_by_category', Product_Categories, 'product_by_category')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

