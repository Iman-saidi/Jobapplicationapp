from django.urls import path
from .views import SignUpView

urlpatterns = [
    # User signup page
    path('signup/', SignUpView.as_view(), name='signup'),
]
    
