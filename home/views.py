from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Welcome " + username + "!"))
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error login In, Try Again..."))
            return redirect('login')
    
    else:
        return render(request, 'shopping/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged out!"))
    return redirect('home')

# TODO: Добавить email в форму регистрации

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull!"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'members/register_user.html', {
        'form':form,
    })

# Create your views here.
def home_page(request):
    return render(request, 'shopping/shop.html')

def checkout_page(request):
    return render(request, 'shopping/cheackout.html')

def cart_page(request):
    return render(request, 'shopping/cart.html')

def bestseller_page(request):
    return render(request, 'shopping/bestseller.html')

def single_page(request):
    return render(request, 'shopping/single.html')

def error_404_page(request):
    return render(request, 'shopping/404.html', status=404)