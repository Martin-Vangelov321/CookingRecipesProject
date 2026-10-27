from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from recipes.models import Recipe
from recipes.forms import RecipeCreateForm, RecipeUpdateForm, RecipeDeleteForm


class RecipesDetailsListView(ListView):
    queryset = (
        Recipe.objects
            .prefetch_related('recipe_ingredients', 'comments')
            .select_related('chef')
            .order_by('-created_at')
    )

    context_object_name = 'recipes'
    paginate_by = 3
    template_name = 'recipes/recipes-details-list.html'

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(recipe_name__icontains=query)

        return queryset

def recipe_details(request: HttpRequest, slug) -> HttpResponse:
    recipe = (
        Recipe.objects
        .prefetch_related('recipe_ingredients', 'comments')
        .select_related('chef').get(slug=slug))

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe-details.html', context)


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/recipe-add.html'

    def get_success_url(self):
        return reverse_lazy('recipes:details-single', kwargs={'slug': self.object.slug})


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipes/recipe-update.html'

    def get_success_url(self):
        return reverse_lazy('recipes:details-single', kwargs={'slug': self.object.slug})


def recipe_delete_view(request: HttpRequest, slug: str) -> HttpResponse:
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:details')

    form = RecipeDeleteForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe-delete.html', context)