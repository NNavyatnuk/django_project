from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'shopping/shop.html')

def checkout_page(request):
    return render(request, 'shopping/cheackout.html')

def cart_page(request):
    return render(request, 'shopping/cart.html')

def bestseller_page(request):
    return render(request, 'shopping/bestseller.html')

def error_404_page(request):
    return render(request, 'shopping/404.html')

def single_page(request):
    return render(request, 'shopping/single.html')
