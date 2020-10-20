from django.shortcuts import render, redirect
# from .models import Category, Guide
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'main/index.html')



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You've are now logged in as {username}")
                redirect('main:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form':form})


def logout_request(request):
    logout(request)
    messages.info(request, "You've logged out successfully")
    return redirect('main:homepage')

