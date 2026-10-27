from django.contrib import admin
from recipes.models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ['recipe_name', 'prepare_time_in_minutes', 'servings', 'chef', 'created_at']
    search_fields = [
        'recipe_name', 'chef__first_name', 'chef__last_name',
        'prepare_time_in_minutes', 'recipe_ingredients__ingredient_name'
    ]
    list_filter = ['servings', 'chef']
