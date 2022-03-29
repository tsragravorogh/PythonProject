from django.urls import path

from . import views

urlpatterns = [
    path('', views.foods, name='food'),
    path('create/', views.create, name='create_food')
]