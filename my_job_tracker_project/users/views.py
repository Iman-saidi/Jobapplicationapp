from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.http import HttpResponse
from django.shortcuts import render

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home") 
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def home(request):
    return HttpResponse("Welcome to Job Tracker!")

def user_list(request):
    return HttpResponse("Users page - list of users")

def user_detail(request, pk):
    return HttpResponse(f"User detail page for ID {pk}")

def user_list(request):
    return render(request, 'users/list.html')

def user_detail(request, pk):
    return render(request, 'users/detail.html', {'id': pk})
