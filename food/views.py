from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import DetailView, DeleteView

from food.models import Food
from food.forms import FoodForm


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food/food_detatils.html'
    context_object_name = 'food'


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food/food_delete.html'
    success_url = 'food.html'


def foods(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }

    return render(request, 'food/food.html', context)


def create(request):
    error = ''
    if request.POST:
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = form.errors
    form = FoodForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'food/create_food.html', context)