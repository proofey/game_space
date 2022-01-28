from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('register/', views.registration_request, name='registration')
]