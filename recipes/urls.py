from django.urls import path, include

from recipes.views import RecipesDetailsListView, recipe_details, RecipeCreateView, RecipeUpdateView, recipe_delete_view

app_name = 'recipes'

urlpatterns = [

    path('list/', RecipesDetailsListView.as_view(), name='details'),

    #path('details/<int:recipe_id>/', recipe_details, name='details-single'),
    path('add/', RecipeCreateView.as_view(), name='create'),
    #path('update/<int:pk>/', RecipeUpdateView.as_view(), name='update'),
   # path('delete/<int:pk>/', recipe_delete_view, name='delete'),

    path('<slug:slug>/', include([
        path('update/', RecipeUpdateView.as_view(), name='update'),
        path('delete/', recipe_delete_view, name='delete'),
        path('details/', recipe_details, name='details-single'),
    ]))
]
