from rest_framework import serializers
from food.models import Food

class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Food
		fields = ('food_id','title','description','status', 'image')