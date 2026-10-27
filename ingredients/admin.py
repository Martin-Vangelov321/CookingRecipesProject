from django.contrib import admin
from ingredients.models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'ingredient_name', 'grams', 'total_calories',
        'total_protein', 'total_fats', 'total_carbohydrates',
        'category', 'is_vegan', 'is_gluten_free'
    ]

    search_fields = ['ingredient_name', 'category']
    list_filter = ['ingredient_name', 'is_vegan', 'is_gluten_free']
