from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.category_guides, name='category_guides'),
    path('guides/<slug:slug>/', views.specific_guide, name='specific_guide'),
]

