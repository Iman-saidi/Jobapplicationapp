from django.urls import path
from .views import SignUpView  # You must import the class here

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]    
