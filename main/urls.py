from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
]

