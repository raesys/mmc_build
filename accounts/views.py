from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Profile, Project

from django.contrib.auth.models import User



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
                return redirect('main:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You've logged out successfully")
    return redirect('accounts:login')


### Dashboard
def dashboard(request):
    current_user = request.user
    print(current_user)
    user_profile = get_object_or_404(User, username=current_user)
    # user_profile = get_object_or_404(Profile, user=current_user)
    user_projects = Project.objects.filter(created_by=current_user)

    context = {
        'user_profile': user_profile,
        'user_projects': user_projects
    }

    return render(request, 'accounts/dashboard.html', context)
