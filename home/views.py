from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'shopping/shop.html')

def checkout_page(request):
    return render(request, 'shopping/cheackout.html')