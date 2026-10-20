from django import forms

from common.mixins import DisableFormMixin
from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['slug', 'created_at', 'updated_at']

        widgets = {
            'recipe_name': forms.TextInput(attrs={'placeholder': 'Enter recipe name'}),
            'dish_photo': forms.URLInput(attrs={'placeholder': 'Link to dish photo'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter instructions'}), #row set?
            'prepare_time_in_minutes': forms.NumberInput(attrs={'placeholder': 'Enter preparation time'}),
            'servings': forms.NumberInput(attrs={'placeholder': 'Enter servings'}),
        }

        error_messages = {
            'recipe_name': {
                'required': 'Recipe Name cannot be empty',
            },
            'dish_photo': {
                'required': 'Enter url link to dish photo',
            },
            'instructions': {
                'required': 'Instructions are required',
            },
            'prepare_time_in_minutes': {
                'required': 'This field cannot be empty',
            },
            'servings': {
                'required': 'This field cannot be empty',
            }
        }

class RecipeCreateForm(RecipeBaseForm):
    ...

class RecipeUpdateForm(RecipeBaseForm):
    ...

class RecipeDeleteForm(DisableFormMixin ,RecipeBaseForm):
    ...