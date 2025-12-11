from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('checkout', checkout_page, name='checkout'),
    path('cart', cart_page, name='cart'),
    path('bestseller', bestseller_page, name='bestseller'),
    path('single', single_page, name='single'),
    path('login_user', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register_user', register_user, name='register_user'),
    re_path(r'^.*$', error_404_page, name='404'),
]