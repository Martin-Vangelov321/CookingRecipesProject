from django.urls import path, include
from ingredients.views import IngredientsDetailsListView, IngredientCreateView, IngredientUpdateView, \
    ingredient_delete_view

app_name = 'ingredients'

urlpatterns = [

    path('list/', IngredientsDetailsListView.as_view(), name='details'),
    path('add/', IngredientCreateView.as_view(), name='create'),

    path('<int:pk>', include([
        path('update/', IngredientUpdateView.as_view(), name='update'),
        path('delete/', ingredient_delete_view, name='delete'),
    ]))


]