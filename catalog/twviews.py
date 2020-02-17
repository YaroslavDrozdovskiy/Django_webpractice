# from django.shortcuts import render
# from django.http import HttpResponse, Http404
from catalog.models import Category, Good
from django.core.paginator import Paginator, InvalidPage
from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class CategoryListMixin(ContextMixin):
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by('name')
        return context
    



class GoodListView(ListView, CategoryListMixin):
    template_name = "index.html"
    queryset = Good.objects.order_by("name")
    paginate_by = 2
    cat = None

    # присваивает переменной контекста данных,в которой должен находиться список значений, этот самый список
    def get(self, request, *args, **kwargs):
        if self.kwargs['cat_id'] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk=self.kwargs["cat_id"])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        context['category'] = self.cat
        return context

    def get_queryset(self):

        return Good.objects.filter(category=self.cat).order_by("name")


class GoodDetailView(DetailView, CategoryListMixin):
    template_name = 'good.html'
    model = Good
    pk_url_kwarg = 'good_id'

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context['pn'] = self.request.GET['page']
        except KeyError:
            context['pn'] = 1
        context['cats'] = Category.objects.order_by('name')

        return context

