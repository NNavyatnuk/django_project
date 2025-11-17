from django.shortcuts import render

def home_page(request):
    return render(request, 'home/home.html')   # шаблон з папки templates/home

def acc(request):
    return render(request, 'ux/acc.html')      # шаблон з папки templates/ux
