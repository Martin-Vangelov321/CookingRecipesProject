from datetime import date

from django import forms
from chefs.models import Chef
from common.mixins import DisableFormMixin


class ChefBaseForm(forms.ModelForm):

    class Meta:
        model = Chef
        exclude = ['slug', 'created_at']


        labels = {
            'first_name': 'Chef first name',
            'last_name': 'Chef last name',
            'is_head_chef': 'Head chef',
            'country': 'Chef country',
            'bio': 'Chef biography',
        }


        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter Chef First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Chef Last Name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Enter Chef Bio', 'rows': 10}),
            'birth_year': forms.NumberInput(attrs={'placeholder': 'Enter Chef Birth Year'}),
            'specialty': forms.TextInput(attrs={'placeholder': 'Enter Chef Specialty'}),
        }

        error_messages = {
            'first_name': {
                'required': 'Chef First Name Cannot Be Blank',
                'max_length': 'Chef First Name Must Be Smaller Than 30 characters',
                'min_length': 'Chef First Name Must Be Bigger Than 2 characters',
            },
            'last_name': {
                'required': 'Chef Last Name Cannot Be Blank',
                'max_length': 'Chef Last Name Must Be Smaller Than 30 characters',
                'min_length': 'Chef Last Name Must Be Bigger Than 2 characters',
            },


        }


    def clean_birth_year(self):
        birth_year = self.cleaned_data['birth_year']
        youngest_allowed_year = date.today().year - 18
        oldest_allowed_year = date.today().year - 80


        if birth_year < oldest_allowed_year:
            raise forms.ValidationError('Chef cannot be older than 80 years')

        if birth_year > youngest_allowed_year:
            raise forms.ValidationError('Chef must be at lest 18 years old.')

        return birth_year


class ChefCreateForm(ChefBaseForm):
    ...

class ChefUpdateForm(ChefBaseForm):
    ...

class ChefDeleteForm(DisableFormMixin, ChefBaseForm):
    ...