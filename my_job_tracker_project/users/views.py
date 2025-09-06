from django.shortcuts import render
from django.contrib.auth import get_user_model

def users_list(request):

    User = get_user_model()
    all_users = User.objects.all()

    context = {
        'users': all_users,
    }

    return render(request, 'users_list.html', context)

def home(request):
    return render(request, 'home.html')
