from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applications_home'),
    path('', views.application_list, name='application_list'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
]
