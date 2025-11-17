# shop/urls.py
from django.urls import path
from .views import home_page, acc

urlpatterns = [
    path('', home_page, name='home'),   # http://127.0.0.1:8000/
    path('acc/', acc, name='acc'),      # http://127.0.0.1:8000/acc/
]
