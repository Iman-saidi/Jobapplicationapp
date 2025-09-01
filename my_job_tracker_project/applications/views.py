from django.http import HttpResponse
from django.shortcuts import render

def application_list(request):
    return HttpResponse("Applications page - list of job applications")

def application_detail(request, pk):
    return HttpResponse(f"Application detail page for ID {pk}")

def application_list(request):
    return render(request, 'applications/list.html')

def application_detail(request, pk):
    return render(request, 'applications/detail.html', {'id': pk})

def index(request):
    return HttpResponse("Welcome to the Applications Home Page")
