from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, Category, Series
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm


def homepage(request):
    return render(request, 'main/categories.html', {'categories': Category.objects.all})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"New account created: {username}")
            return redirect('main:homepage')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request, 'main/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, f"Logged out successfully")
    return redirect('main:homepage')

def login_request(request):
    if request.user == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('main:homepage')
            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def single_slug(request, single_slug):
    categories = [c.slug for c in Category.objects.all()]
    if single_slug in categories:
        matching_series = Series.objects.filter(category__slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(series__title=m.title).earliest('published')
            series_urls[m] = part_one.slug

        return render(request, 'main/category.html', {'tutorial_series': matching_series, 'part_ones': series_urls})

    tutorials = [t.slug for t in Tutorial.objects.all()]
    
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(series__title=this_tutorial.series).order_by('published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request, 'main/tutorial.html', {'tutorial': this_tutorial, 'sidebar': tutorials_from_series, 'this_tut_idx': this_tutorial_idx})
    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")