from django.forms.models import modelformset_factory
from django.views.generic.base import TemplateView
from .models import Category
from django.shortcuts import redirect

CategoryFormset = modelformset_factory(
    Category, labels={'name': "Название"}, fields='__all__', can_order = True, can_delete = True)


class CategoryListView(TemplateView):
    # обработка набора форм для категорий товаров
    
    template_name = 'cats.html'
    formset = None

    def get(self, request, *args, **kwargs):
        self.formset = CategoryFormset()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.formset
        return context

    def post(self, request, *args, **kwargs):
        self.formset = CategoryFormset(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            return redirect('catalog:cats')
        else:
            return super().get(request, *args, **kwargs)
