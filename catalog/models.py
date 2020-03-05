from django.db import models
from django.db.models import Q

# Create your models here.


class Category(models.Model):
    # категории товаров

    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Good(models.Model):

    # хранение списка товаров
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Название")
    description = models.TextField(
        default='', verbose_name='Описание товара')
    price = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Цена")
    in_stock = models.BooleanField(
        default=True, db_index=True, verbose_name="В наличии")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    # метаданные таблицы

    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        s = self.name
        if not self.in_stock:
            return s + " (нет в наличии)"
        return s


class BlogArticle(models.Model):
    title = models.CharField(max_length=50, unique_for_month="pubdate")
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)


class New(models.Model):
    title = models.CharField("Оглавление", max_length=100, db_index=True)
    description = models.TextField("Описание")
    content = models.TextField("Контент")
    pub_date = models.DateField("Дата публикации", db_index = True, auto_now_add=True)

    def __str__(self):
        return self.title