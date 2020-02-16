from django.shortcuts import render
from django.http import HttpResponse, Http404
from catalog.models import Category, Good
from django.core.paginator import Paginator

# Create your views here.


def index(request, cat_id):
    """
    каталог товаров
    """
    # возвращает значение ключа,если его нет,то не бросает исключение ,а None
    page_num = request.GET.get('page')

    # if page_num is None:
    #     page_num = 1
    
    cats = Category.objects.all().order_by("name")
    # получение категории по введённому id
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=cat_id)
    # получение списка товаров и инициализация пагинатора
    paginator = Paginator(Good.objects.filter(
        category=cat).order_by("name"), 2)

    # формирование объекта Page

    goods = paginator.get_page(page_num)

    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods})


def good(request, good_id):
    # описание товара
    page_num = request.GET.get('page')
    if page_num is None:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404

    return render(request, "good.html", {"cats": cats, "good": good, "pn": page_num})
