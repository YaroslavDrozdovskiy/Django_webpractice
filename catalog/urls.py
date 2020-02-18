from django.urls import path
from .twviews import GoodListView, GoodDetailView, NewArchiveView


app_name = 'catalog'

urlpatterns = [
    path('<int:cat_id>', GoodListView.as_view(), name="index"),
    path('good/<int:good_id>', GoodDetailView.as_view(), name="good"),
    path('news/', NewArchiveView.as_view(), name="news_archive" ),

]