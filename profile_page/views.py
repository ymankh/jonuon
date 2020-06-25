from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'wrong email or password')
            return redirect('login')
        password = request.POST['password']
        username = user.username
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In Successfully')
            return redirect('homepage')
        else:
            messages.error(request, 'wrong email or password')
        return redirect('login')

    return render(request, 'login_page.html')


def signup(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error messages')
        return redirect('signup')
    return render(request, 'signup_page.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')
