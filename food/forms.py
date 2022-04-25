from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, FileInput, Textarea, Select

from .models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'brand', 'price', 'date', 'description', 'weight', 'type', 'image']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'brand': Select(attrs={
                'class': 'form-control',
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
            'weight': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weight',
            }),
            'type': Select(attrs={
                'class': 'form-control',
            }),
            'image': FileInput()
        }