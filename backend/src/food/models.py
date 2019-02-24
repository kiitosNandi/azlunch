from django.db import models

# Create your models here.

class Food(models.Model):
	food_id 	= models.AutoField(primary_key=True)
	title 		= models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	status 		= models.BooleanField(default=True)
	image 		= models.ImageField()

	def __str__(self):
		return self.title