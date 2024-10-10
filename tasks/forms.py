from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Task

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'status', 'due_date', 'priority']
