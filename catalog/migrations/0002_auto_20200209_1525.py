# Generated by Django 3.0.3 on 2020-02-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена'),
        ),
    ]
