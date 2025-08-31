from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import JobApplication
from .forms import JobApplicationForm
class DashboardView(LoginRequiredMixin, generic.TemplateView):
template_name = 'dashboard.html'
def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs)
qs = JobApplication.objects.filter(user=self.request.user)
context['total'] = qs.count()
context['by_status'] =
qs.values('status').order_by().annotate(count=models.Count('status'))

context['recent'] = qs[:5]
return context
class ApplicationListView(LoginRequiredMixin, generic.ListView):
model = JobApplication
template_name = 'applications/application_list.html'
context_object_name = 'applications'
def get_queryset(self):
return JobApplication.objects.filter(user=self.request.user)
class ApplicationDetailView(LoginRequiredMixin, UserPassesTestMixin,
generic.DetailView):
model = JobApplication
template_name = 'applications/application_detail.html'
def test_func(self):
obj = self.get_object()
return obj.user == self.request.user
class ApplicationCreateView(LoginRequiredMixin, generic.CreateView):
model = JobApplication
form_class = JobApplicationForm
template_name = 'applications/application_form.html'
success_url = reverse_lazy('applications:list')
def form_valid(self, form):
form.instance.user = self.request.user
return super().form_valid(form)
class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin,
generic.UpdateView):
model = JobApplication
form_class = JobApplicationForm
template_name = 'applications/application_form.html'
def get_success_url(self):
return reverse_lazy('applications:detail', kwargs={'pk':
self.object.pk})
def test_func(self):
obj = self.get_object()
return obj.user == self.request.user
class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin,
generic.DeleteView):
model = JobApplication
template_name = 'applications/application_confirm_delete.html'

success_url = reverse_lazy('applications:list')
def test_func(self):
obj = self.get_object()
return obj.user == self.request.user
