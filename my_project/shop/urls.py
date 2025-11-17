# shop/urls.py
from django.urls import path
from .views import home_page

urlpatterns = [
    path('', home_page, name='home'),   # http://127.0.0.1:8000/     
]
