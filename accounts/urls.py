from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.update_profile, name='update_profile'),
    path('message/', views.message_mentor, name='message_mentor'),
]

