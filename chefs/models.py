from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


class Chef(models.Model):

    class ChefCountryChoices(models.TextChoices):
        BULGARIA = 'BULGARIA', 'Bulgaria'
        ENGLAND = 'ENGLAND', 'England'
        USA = 'USA', 'USA'
        GREECE = 'GREECE', 'Greece'
        ITALIAN = 'ITALIA', 'Italia'
        SPAIN = 'SPAIN', 'Spain'
        FRANCE = 'FRANCE', 'France'
        GERMANY = 'GERMANY', 'Germany'

    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    country = models.CharField(max_length=30, choices=ChefCountryChoices.choices)
    bio = models.TextField(max_length=600, null=True, blank=True)
    birth_year = models.PositiveIntegerField()
    is_head_chef = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, editable=False, blank=True, null=False)


    @property
    def age(self):
        age = date.today().year - self.birth_year
        return age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f'{self.first_name}-{self.last_name}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
