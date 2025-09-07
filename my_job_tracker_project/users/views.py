from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.http import JsonResponse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'

def user_list(request):
    data = [
        {"id": 1, "username": "iman"},
        {"id": 2, "username": "summeiya"},
    ]
    return JsonResponse(data, safe=False)    
