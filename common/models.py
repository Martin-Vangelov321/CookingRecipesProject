from django.db import models


class Comment(models.Model):
    text = models.TextField(max_length=400)
    date_and_time = models.DateTimeField(auto_now_add=True)
    to_recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-date_and_time']


class SavedRecipes(models.Model):
    to_recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
