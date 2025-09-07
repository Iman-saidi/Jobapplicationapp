from django.urls import path
from .views import SignUpView  
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("", views.user_list, name="user-list"),
    path("profile/", views.profile_view, name="profile"),
]    
