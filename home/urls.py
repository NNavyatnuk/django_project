# my_project/urls.py (всередині папки my_project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),   # підключаємо всі шляхи з shop/urls.py
]
