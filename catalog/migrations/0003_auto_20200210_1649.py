# Generated by Django 3.0.3 on 2020-02-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200209_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(default='', verbose_name='Описание товара'),
        ),
    ]
