from decimal import Decimal

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


class Ingredient(models.Model):

    CALORIES_PER_GRAM_PROTEIN = 4
    CALORIES_PER_GRAM_CARB = 4
    CALORIES_PER_GRAM_FAT = 9

    class CategoryChoices(models.TextChoices):
        VEGETABLE = 'Vegetable', 'Vegetable'
        FRUIT = 'Fruit', 'Fruit'
        MEAT = 'Meat', 'Meat'
        DAIRY = 'Dairy', 'Dairy'
        SPICE = 'Spice', 'Spice'
        GRAIN = 'Grain', 'Grain'
        OTHER = 'Other', 'Other'


    ingredient_name = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    grams = models.IntegerField(validators=[MinValueValidator(1)])

    calories_per_100gr = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.1'))]
    )

    protein_per_100gr = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.1'))]
    )

    carbohydrates_per_100gr = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.1'))]
    )

    fats_per_100gr = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.1'))]
    )

    category = models.CharField(max_length=120, choices=CategoryChoices.choices, default=CategoryChoices.OTHER)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)

    @property
    def total_protein(self):
        result = (self.protein_per_100gr * self.grams) / 100
        return result.quantize(Decimal('0.1'))

    @property
    def total_carbohydrates(self):
        result = (self.carbohydrates_per_100gr * self.grams) / 100
        return result.quantize(Decimal('0.1'))

    @property
    def total_fats(self):
        result = (self.fats_per_100gr * self.grams) / 100
        return result.quantize(Decimal('0.1'))

    @property
    def total_calories(self):
        result = (
            (self.total_protein * self.CALORIES_PER_GRAM_PROTEIN) +
            (self.total_carbohydrates * self.CALORIES_PER_GRAM_CARB) +
            (self.total_fats * self.CALORIES_PER_GRAM_FAT)
        )
        return result.quantize(Decimal('0.1'))

    def __str__(self):
        return self.ingredient_name
