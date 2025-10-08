from django.urls import path
from .views import home_page  

urlpatterns = [
    path("", views.index, name="home-index"),
]
