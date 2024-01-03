# forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row
from django import forms

from .models import Branch


class StudentRegistrationForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    name = forms.CharField(max_length=200)
    surname = forms.CharField(max_length=200)
    dateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('branch', css_class='w-full md:w-1/2 pr-4'),
                Column('name', css_class='w-full md:w-1/2 pl-4'),
            ),
            Row(
                Column('surname', css_class='w-full md:w-1/2 pr-4'),
                Column('date_of_birth', css_class='w-full md:w-1/2 pl-4'),
            ),
            'image',
        )
