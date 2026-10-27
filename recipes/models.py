from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    dish_photo = models.URLField()
    instructions = models.TextField()
    prepare_time_in_minutes = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    servings = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    chef = models.ForeignKey('chefs.Chef', on_delete=models.SET_NULL, null=True)
    recipe_ingredients = models.ManyToManyField(to='ingredients.Ingredient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False, blank=True, null=False)


    @property
    def recipe_total_calories(self):
        return sum(ingredient.total_calories for ingredient in self.recipe_ingredients.all())

    @property
    def recipe_total_protein(self):
        return sum(ingredient.total_protein for ingredient in self.recipe_ingredients.all())

    @property
    def recipe_total_fats(self):
        return sum(ingredient.total_fats for ingredient in self.recipe_ingredients.all())

    @property
    def recipe_total_carbohydrates(self):
        return sum(ingredient.total_carbohydrates for ingredient in self.recipe_ingredients.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f'{self.recipe_name}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.recipe_name
