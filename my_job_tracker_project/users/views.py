from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'
    
def user_list(request):
    users = [
        {"id": 1, "username": "iman"},
        {"id": 2, "username": "summeiya"},
    ]
    return render(request, "users/user_list.html", {"users": users})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after a successful signup
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, "users/profile.html")
