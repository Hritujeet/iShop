from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Logged in Successfully | Continue Your Shopping with iShop")
        return redirect('home')

    return render(request, "user/login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confPass = request.POST.get('confPass')

        if len(username)>=3 and len(password)>=8 and password == confPass:
            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.save()
            messages.add_message(request, messages.SUCCESS, "Your account has been created succesfully!")
            return redirect('home')

    return render(request, "user/signup.html")

def handleLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out Succesfully")
    return redirect('home')
