from django.db import models
from rest_framework import serializers
from userdetail.models import User, Vehicle

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('state','gender','first_name','last_name')

class UserVehicle(serializers.ModelSerializer):
	class Meta:
		model = Vehicle
		fields = ('vehicle_name')