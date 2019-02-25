from rest_framework import viewsets
from food.models import Food
from .serializers import FoodSerializer

class FoodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing food instances.
    """
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


""" Old way of doing things"""

# from rest_framework.generics import (
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	CreateAPIView,
# 	DestroyAPIView,
# 	UpdateAPIView,
# )



# class FoodListView(ListAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer

# class FoodDetailView(RetrieveAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer

# class FoodCreateView(CreateAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer

# class FoodUpdateView(UpdateAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer

# class FoodDeleteView(DestroyAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer

