from django.contrib import admin
from catalog.models import Category, Good, New

# Register your models here.
admin.site.register(Category)
admin.site.register(Good)
admin.site.register(New)