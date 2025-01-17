from django import forms
from .models import Category, Good

# Django формы


class GoodForm(forms.ModelForm):
    
    name = forms.CharField(
        label='Название', help_text='Должно быть уникальным')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), label="Категория", empty_label=None)
    in_stock = forms.BooleanField(initial= True, label = 'Есть в наличии')

    class Meta:
        model = Good
        fields = '__all__'
        # fields= [], exclude = []