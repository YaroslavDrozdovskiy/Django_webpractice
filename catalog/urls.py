from django.urls import path
from .views import index, good

app_name = 'catalog'

urlpatterns = [
    path('<int:cat_id>', index, name="index"),
    path('good/<int:good_id>', good, name="good")

]