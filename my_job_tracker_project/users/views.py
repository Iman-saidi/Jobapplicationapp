from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # redirect after signup
        return render(request, "signup.html", {"form": form})
