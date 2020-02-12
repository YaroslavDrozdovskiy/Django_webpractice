# Generated by Django 3.0.3 on 2020-02-09 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique_for_month='pubdate')),
                ('pubdate', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(default='haha', verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='В наличии')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-price', 'name'],
                'unique_together': {('category', 'name', 'price')},
            },
        ),
    ]
