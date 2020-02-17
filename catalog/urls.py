from django.urls import path
from .twviews import GoodListView, GoodDetailView
from .views import index, good


app_name = 'catalog'

urlpatterns = [
    path('<int:cat_id>', GoodListView.as_view(), name="index"),
    path('good/<int:good_id>', GoodDetailView.as_view(), name="good"),
    # path('about/', AboutView.as_view(template_name='others/about.html'), name = 'about')

]