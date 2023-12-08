from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'more_description', 'status', 'due_date']
        widgets = {
            'status': forms.Select(choices=Task.STATUS_CHOICES)
        }
