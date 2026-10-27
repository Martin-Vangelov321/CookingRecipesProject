from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from common.models import Comment
from recipes.models import Recipe
from common.forms import CommentForm



def home_page_view(request:HttpRequest) -> HttpResponse:

    last_recipes = (
        Recipe.objects.prefetch_related('recipe_ingredients')
        .select_related('chef')
        .order_by('-created_at')
    )[:3]

    context = {
        'last_recipes': last_recipes,
    }

    return render(request, 'common/home-page.html', context=context)

def add_comment_view(request: HttpRequest, recipe_id: int) -> HttpResponse:
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_recipe = recipe
            comment.save()

        return redirect(request.META.get('HTTP_REFERER'))

def delete_comment_view(request: HttpRequest, comment_id: int) -> HttpResponse:

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()


    return redirect(request.META.get('HTTP_REFERER'))
