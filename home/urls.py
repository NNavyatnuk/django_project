from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('checkout', checkout_page, name='checkout'),
]