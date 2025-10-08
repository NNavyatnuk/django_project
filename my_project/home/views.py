from django.shortcuts import render

def index(request):
    return HttpResponse("Привіт! Це додаток Home.")
