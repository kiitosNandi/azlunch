from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView, 
	CreateAPIView,
	DestroyAPIView,
	UpdateAPIView,
)

from food.models import Food
from .serializers import FoodSerializer


class FoodListView(ListAPIView):
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

class FoodDetailView(RetrieveAPIView):
	que