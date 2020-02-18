from catalog.models import Category, Good, New
from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.core.urlresolvers import reverse


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


class NewArchiveView(ArchiveIndexView):
    model = New
    date_field = "pub_date"
    template_name = 'news_archive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        return context


################## простые формы ##################################

class GoodEditMixin(CategoryListMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['pn'] = self.request.GET["page"]
        except KeyError:
            context['pn'] = 1

        return context


class GoodEditView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]
        except KeyError:
            pn = 1
        slef.success_url = self.success_url + "?page=" + pn
        
        return super().post(self, request, *args, **kwargs)
    
class GoodCreate(CreateView, GoodEditMixin):
    
