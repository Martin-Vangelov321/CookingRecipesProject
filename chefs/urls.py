from django.urls import path, include

from chefs.views import ChefsDetailsListView, ChefCreateView, chef_details_view, ChefUpdateView, chef_delete_view

app_name = 'chefs'

urlpatterns = [

    path('list/', ChefsDetailsListView.as_view(), name='details'),
    path('add/', ChefCreateView.as_view(), name='add'),

    path('<slug:slug>/', include([
        path('update/', ChefUpdateView.as_view(), name='update'),
        path('delete/', chef_delete_view, name='delete'),
        path('details/', chef_details_view, name='details-single'),
    ]))
]






























































