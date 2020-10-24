from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import ProfileForm, ChatForm


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
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


@login_required(login_url='accounts:login')
def dashboard(request):
    current_user = request.user
    # user_profile = get_object_or_404(Profile, user=current_user)
    try:
        user_profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        user_profile = None
    user_projects = Project.objects.filter(created_by=current_user)

    context = {
        'user_profile': user_profile,
        'user_projects': user_projects
    }
    return render(request, 'accounts/dashboard.html', context)


def update_profile(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.info(request, "You have successfully updated your profile")
            return redirect('accounts:dashboard')
    else:
        form = ProfileForm(instance=user_profile)

    context = {
        'form': form
    }
    return render(request, 'accounts/update_profile.html', context)


@login_required(login_url='accounts:login')
def message_mentor(request):
    if request.method == 'POST':
        form = ChatForm(data=request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.save()
            messages.info(request, "Your message has been sent.")
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "You have missed out required fields")
    else:
        form = ChatForm()
     
    context = {
        'form': form
    }
    return render(request, 'accounts/message_mentor.html', context)
