# home/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привіт! Це додаток Home.")
