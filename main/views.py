from django.shortcuts import render, get_object_or_404
from .models import Category, Guide



def homepage(request):
    return render(request, 'main/homepage.html')


def categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'main/categories.html', context)


def category_guides(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_guides = category.guide_set.all()
    # category_guides = get_object_or_404(Category, slug=slug).guide_set.all()
    context = {
        'category_guides': category_guides
    }
    return render(request, 'main/category_guides.html', context)
    

def specific_guide(request, slug):
    guide = get_object_or_404(Guide, slug=slug)

    # tutorials_from_series = Guide.objects.filter(category__name=guide.category).order_by('published_date')
    guides_from_category = Guide.objects.filter(category=guide.category).order_by('published_date')

    context = {
        'guide': guide,
        'sidebar': guides_from_category,
    }
    return render(request, 'main/specific_guide.html', context)
    