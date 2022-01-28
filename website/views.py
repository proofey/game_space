from django.shortcuts import render, redirect
from .models import Intro
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . utils import anonymous_required



def home_page(request):
    intros = Intro.objects.all()

    login_form = LoginForm()
    registration_form = RegistrationForm()

    return render(request, 'website/homepage.html', {
        'intros': intros,
        'login_form': login_form,
        'registration_form': registration_form
    })

def logout_request(request):
    logout(request)
    messages.info(request, "You are now logged out!")
    return redirect('home-page')


@anonymous_required
def registration_request(request):
    registration_form = RegistrationForm()
    
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, f"Your registration was successful!You can now log in.")
            return redirect('login')
        else:
            messages.error(request, f"You didnt pass some of the registration requirements...please try again.")        
            return redirect('registration')

    return render(request, 'website/registration.html', {
        'registration_form': registration_form
    })


@anonymous_required
def login_request(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged as {username}")
                return redirect('home-page')
        else:
            messages.error(request, f"Invalid 'Username' or 'Password'")
            return redirect('login')
    
    return render(request, 'website/login.html', {
        'login_form': login_form
    })