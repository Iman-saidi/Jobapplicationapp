from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm

def index(request):
    return HttpResponse("Welcome to the Applications Home Page")


@login_required
def application_list(request):
    """
    Renders the page to display all job applications for the logged-in user.
    """
    applications = JobApplication.objects.filter(user=request.user).order_by('-application_date')
    context = {
        'applications': applications
    }
    return render(request, 'applications/list.html', context)

@login_required
def application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    context = {
        'application': application
    }

    return render(request, 'applications/detail.html', {'id': pk})

@login_required
def application_create(request):
    """
    Handles creating a new job application.
    """
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.user = request.user
            new_application.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm()

    return render(request, 'applications/create.html', {'form': form})

@login_required
def application_edit(request, pk):
    """
    Handles editing an existing job application.
    """
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_detail', pk=pk)
    else:
        form = JobApplicationForm(instance=application)

    return render(request, 'applications/edit.html', {'form': form, 'application': application})

@login_required
def application_delete(request, pk):
    """
    Handles deleting a job application.
    """
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
        application.delete()
        return redirect('application_list')

    return render(request, 'applications/confirm_delete.html', {'application': application})

