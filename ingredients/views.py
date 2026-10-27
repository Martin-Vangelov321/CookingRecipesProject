from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from ingredients.forms import IngredientCreateForm, IngredientUpdateForm, IngredientDeleteForm
from ingredients.models import Ingredient


# Create your views here.


class IngredientsDetailsListView(ListView):
    queryset = (
        Ingredient.objects.all().order_by('-created_at')
    )
    context_object_name = 'ingredients'
    paginate_by = 3
    template_name = 'ingredients/ingredients-details-list.html'

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(ingredient_name__icontains=query)


        return queryset


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'ingredients/ingredient-create.html'
    success_url = reverse_lazy('ingredients:details')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'ingredients/ingredient-update.html'
    success_url = reverse_lazy('ingredients:details')

def ingredient_delete_view(request: HttpRequest, pk:int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredients:details')

    form = IngredientDeleteForm(instance=ingredient)

    context = {
        'form': form,
        'ingredient': ingredient,
    }

    return render(request, 'ingredients/ingredient-delete.html', context)