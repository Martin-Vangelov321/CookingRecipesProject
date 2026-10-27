from django.urls import path
from common import views
from common.views import add_comment_view, delete_comment_view

app_name = 'common'

urlpatterns = [
    path('',views.home_page_view ,name='home'),
    path('comment/add/<int:recipe_id>/', add_comment_view, name='add_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment_view, name='delete_comment'),
]
