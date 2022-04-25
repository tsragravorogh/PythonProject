from django.urls import path

from . import views
from .views import FoodDetailView

urlpatterns = [
    path('', views.foods, name='food'),
    path('create/', views.create, name='create_food'),
    path('<int:pk>', FoodDetailView.as_view(), name='food_details'),
    path('<int:pk>/delete', views.FoodDeleteView.as_view(), name='food_delete'),
]