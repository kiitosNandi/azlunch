from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
	user_id 		= models.AutoField(primary_key=True)
	first_name 		= models.CharField(max_length=225)
	last_name		= models.CharField(max_length=225)
	other_name		= models.CharField(max_length=225, blank=True)
	company_name 	= models.CharField(max_length=225)
	phone_number 	= PhoneNumberField(null=False, blank=False, unique=True)
	email			= models.CharField(max_length=120)

	@property
	def full_name(self):
		return '%s %s' % (self.first_name, self.last_name, self.other_name)

	def __s