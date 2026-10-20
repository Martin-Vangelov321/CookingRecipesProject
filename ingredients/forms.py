from django import forms

from common.mixins import DisableFormMixin
from ingredients.models import Ingredient


class IngredientBaseForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = '__all__'

        labels = {
            'is_vegan' : 'Vegan',
            'is_gluten_free' : 'Gluten free',
        }

        widgets = {
            'ingredient_name':
                forms.TextInput(attrs={'placeholder': 'Enter Ingredient Name'}),

            'grams':
                forms.NumberInput(attrs={'placeholder': 'Enter Ingredient Grams'}),

            'calories_per_100gr':
                forms.NumberInput(attrs={'placeholder': 'Enter Ingredient Calories per 100 gr'}),

            'protein_per_100gr':
                forms.NumberInput(attrs={'placeholder': 'Enter Ingredient Protein per 100 gr'}),

            'fats_per_100gr':
                forms.NumberInput(attrs={'placeholder': 'Enter Ingredient Fats per 100 gr'}),

            'carbohydrates_per_100gr':
                forms.NumberInput(attrs={'placeholder': 'Enter Ingredient Carbohydrates per 100 gr'}),
        }


        error_messages = {
            'ingredient_name': {
                'required': 'Ingredient name cannot be empty',
            },
            'grams': {
                'required': 'Ingredient grams cannot be empty',
                'min_value': 'Grams cannot be zero or less',
            },
            'calories_per_100gr': {
                'required': 'This field cannot be empty',
                'min_value': 'Calories per 100gr cannot be zero',
            },
            'protein_per_100gr': {
                'required': 'This Field Cannot Be Empty',
                'min_value': 'Protein per 100 gr cannot be zero',
            },
            'fats_per_100gr': {
                'required': 'This field cannot be empty',
                'min_value': 'Fats per 100 gr cannot be zero',
            },
            'carbohydrates_per_100gr': {
                'required': 'This field cannot be empty',
                'min_value': 'Carbohydrates per 100 gr cannot be zero',
            }

        }


class IngredientCreateForm(IngredientBaseForm):
    ...

class IngredientUpdateForm(IngredientBaseForm):
    ...

class IngredientDeleteForm(DisableFormMixin ,IngredientBaseForm):
    ...