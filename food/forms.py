from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, Textarea

from .models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['price', 'brand', 'description', 'date']

        widgets = {
            'brand': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brend',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
            'date': DateInput(format="dd.mm.yyyy", attrs={
                'class': 'form-control',
                'placeholder': 'Date',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
            }),
        }
