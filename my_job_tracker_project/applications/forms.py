from django import forms
from .models import JobApplication
class JobApplicationForm(forms.ModelForm):
  application_date = forms.DateField(widget=forms.DateInput(attrs={'type':
'date'}))
  class Meta:
     model = JobApplication
     fields = ['company_name', 'job_title', 'application_date', 'status',
'notes', 'link_to_posting']

