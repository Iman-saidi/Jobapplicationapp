from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Job Tracker!")

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
