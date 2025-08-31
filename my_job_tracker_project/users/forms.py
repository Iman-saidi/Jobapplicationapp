from django import forms
from django.contrib.forms import
UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    classMeta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
