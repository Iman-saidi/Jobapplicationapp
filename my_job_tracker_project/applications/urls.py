from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applications_home'),
    # Later you can add more, e.g.
    # path('create/', views.create_application, name='create_application'),
]

