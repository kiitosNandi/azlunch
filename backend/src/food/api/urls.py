from django.urls import path
from .views import (
	FoodListView, 
	FoodDetailView, 
	FoodCreateView,
	FoodUpdateView,
	FoodDeleteView,
)

urlpatterns = [
	path('',Foo