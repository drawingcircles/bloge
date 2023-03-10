from django.forms import ModelForm

from django import forms
from .models import Project


class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'body',
            'featured_image',
        ]
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input form-control'})
        




