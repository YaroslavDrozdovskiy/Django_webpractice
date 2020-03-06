from django.urls import path
from .catviews import CategoryListView
from .twviews import (
    GoodListView, GoodDetailView, NewArchiveView, 
    GoodCreate, GoodUpdate, GoodDelete,
)

app_name = 'catalog'

urlpatterns = [
    path('<int:cat_id>', GoodListView.as_view(), name="index"),
    path('good/<int:good_id>', GoodDetailView.as_view(), name="good"),
    path('news/', NewArchiveView.as_view(), name="news_archive"),
    path('good/<int:cat_id>/add', GoodCreate.as_view(), name="good_add"),
    path('good/<int:good_id>/edit', GoodUpdate.as_view(), name="good_edit"),
    path('good/<int:good_id>/delete', GoodDelete.as_view(), name="good_delete"),
    path('cats/', CategoryListView.as_view(), name = 'cats')

]
