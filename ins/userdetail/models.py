from django.db import models

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length = 100,unique=True)
	password = models.CharField(max_length = 20)
	state = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 50)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)

	def __str__(self):
		 return self.user_name + ' ' + self.state + ' '+ self.gender +' '+ self.first_name + ' ' + self.last_name 

class Vehicle(models.Model):
	vehicle_name = models.CharField(max_length = 50)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
